# ABOUTME: Generates MP3 narration for a blog post using Kokoro-82M via mlx-audio.
# ABOUTME: Strips markdown, synthesizes speech, adds ID3 tags, updates post frontmatter.

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split post into frontmatter dict and body text."""
    match = re.match(r"^---\n(.*?\n)---\n", text, re.DOTALL)
    if not match:
        raise ValueError("No YAML frontmatter found")
    import yaml

    fm = yaml.safe_load(match.group(1)) or {}
    body = text[match.end() :]
    return fm, body


def strip_markdown(body: str) -> str:
    """Convert markdown body to plain narration text.

    Processing order matters to avoid partial matches on nested syntax.
    """
    text = body

    # 1. HTML comments (<!--more--> etc.)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

    # 2. Fenced code blocks (``` delimited, possibly with language tag)
    text = re.sub(r"```[^\n]*\n.*?```", "", text, flags=re.DOTALL)

    # 3. Images: ![alt](path) — strip entirely (alt text is usually descriptive
    #    metadata, not prose meant to be read aloud)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)

    # 4. Image captions: italic line immediately after an image (standalone *text*)
    #    We keep other italic text; only strip caption-style lines (entire line is italic)
    text = re.sub(r"^\*([^*]+)\*\s*$", "", text, flags=re.MULTILINE)

    # 5. Horizontal rules (--- alone on a line, with optional whitespace)
    #    Replace with paragraph break for TTS pacing
    text = re.sub(r"^\s*---\s*$", "\n", text, flags=re.MULTILINE)

    # 6. Footnote definitions at end of file: [^N]: ... (may span multiple lines)
    text = re.sub(
        r"^\[\^\d+\]:.*?(?=\n\[\^\d+\]:|\n\n|\Z)",
        "",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )

    # 7. Footnote inline references: [^N]
    text = re.sub(r"\[\^\d+\]", "", text)

    # 8. Jekyll/Liquid template tags: {{ ... }}
    text = re.sub(r"\{\{.*?\}\}", "", text)

    # 9. Headers: ## text → \n\ntext\n (preserve text with pacing)
    text = re.sub(r"^#{1,6}\s+(.+)$", r"\n\n\1\n", text, flags=re.MULTILINE)

    # 10. Links: [text](url) → text (handle bold+link combo: **[text](url)** )
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)

    # 11. Bold markers: **text** → text
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)

    # 12. Italic markers: *text* → text (but not mid-word asterisks)
    text = re.sub(r"(?<!\w)\*([^*]+?)\*(?!\w)", r"\1", text)

    # 13. Inline code backticks: `text` → text
    text = re.sub(r"`([^`]+)`", r"\1", text)

    # 14. Remaining HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # 15. Blockquote markers: > at start of line
    text = re.sub(r"^>\s?", "", text, flags=re.MULTILINE)

    # 16. Collapse 3+ newlines to 2 (paragraph spacing for TTS pacing)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # 17. Strip leading/trailing whitespace
    text = text.strip()

    return text


def slug_from_filename(filename: str) -> str:
    """Extract slug: '2026-02-11-a-second-opinion.md' → 'a-second-opinion'."""
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", filename).removesuffix(".md")


def generate_audio(text: str, output_prefix: str, voice: str, speed: float) -> None:
    """Run Kokoro-82M via mlx-audio to generate WAV."""
    from mlx_audio.tts.generate import generate_audio as mlx_generate

    mlx_generate(
        text=text,
        model="mlx-community/Kokoro-82M-bf16",
        voice=voice,
        speed=speed,
        lang_code="a",
        file_prefix=output_prefix,
        audio_format="wav",
        join_audio=True,
        verbose=True,
    )


def convert_to_mp3(wav_path: Path, mp3_path: Path) -> None:
    """Convert WAV to MP3 64kbps mono via ffmpeg."""
    result = subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(wav_path),
            "-codec:a",
            "libmp3lame",
            "-b:a",
            "64k",
            "-ac",
            "1",
            "-ar",
            "24000",
            str(mp3_path),
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"ffmpeg stderr:\n{result.stderr}", file=sys.stderr)
        result.check_returncode()


def add_id3_tags(mp3_path: Path, title: str) -> None:
    """Add Spotify-ready ID3 tags to the MP3."""
    from mutagen.id3 import ID3, TALB, TCON, TIT2, TPE1
    from mutagen.mp3 import MP3

    audio = MP3(str(mp3_path))
    audio.tags = ID3()
    audio.tags.add(TIT2(encoding=3, text=[title]))
    audio.tags.add(TPE1(encoding=3, text=["Gal Sapir"]))
    audio.tags.add(TALB(encoding=3, text=["Sparse Thoughts"]))
    audio.tags.add(TCON(encoding=3, text=["Podcast"]))
    audio.save()


def update_frontmatter(post_path: Path, audio_url: str) -> None:
    """Add or update 'audio:' field in post frontmatter.

    Uses string manipulation (not YAML round-trip) to preserve exact formatting.
    """
    content = post_path.read_text()
    match = re.match(r"^---\n(.*?\n)---\n", content, re.DOTALL)
    if not match:
        raise ValueError(f"No frontmatter found in {post_path}")

    fm_text = match.group(1)
    audio_line = f'audio: "{audio_url}"\n'

    if re.search(r"^audio:", fm_text, re.MULTILINE):
        new_fm = re.sub(r"^audio:.*\n", audio_line, fm_text, flags=re.MULTILINE)
    else:
        new_fm = fm_text + audio_line

    new_content = f"---\n{new_fm}---\n" + content[match.end() :]
    post_path.write_text(new_content)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate audio narration for a blog post"
    )
    parser.add_argument("post", type=Path, help="Path to the markdown post file")
    parser.add_argument("--voice", default="af_heart", help="Kokoro voice name")
    parser.add_argument("--speed", type=float, default=1.0, help="Speech speed")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print stripped text without generating audio",
    )
    parser.add_argument(
        "--skip-frontmatter-update",
        action="store_true",
        help="Don't update the post's frontmatter with audio path",
    )
    args = parser.parse_args()

    if not args.post.exists():
        print(f"File not found: {args.post}", file=sys.stderr)
        sys.exit(1)

    # 1. Read and parse
    text = args.post.read_text()
    frontmatter, body = parse_frontmatter(text)
    narration_text = strip_markdown(body)

    word_count = len(narration_text.split())

    if args.dry_run:
        print(narration_text)
        print(f"\n--- Stats ---")
        print(f"Characters: {len(narration_text)}")
        print(f"Words: {word_count}")
        return

    if word_count < 300:
        print(
            f"Post has only {word_count} words (minimum 300). "
            f"Skipping narration.",
            file=sys.stderr,
        )
        sys.exit(1)

    # 2. Generate audio
    slug = slug_from_filename(args.post.name)
    audio_dir = Path("assets/audio")
    audio_dir.mkdir(parents=True, exist_ok=True)
    mp3_path = audio_dir / f"{slug}.mp3"

    with tempfile.TemporaryDirectory() as tmpdir:
        wav_prefix = str(Path(tmpdir) / "narration")
        print(f"Generating audio with voice={args.voice}, speed={args.speed}...")
        generate_audio(narration_text, wav_prefix, args.voice, args.speed)

        wav_path = Path(f"{wav_prefix}.wav")
        if not wav_path.exists():
            print(f"Expected WAV not found at {wav_path}", file=sys.stderr)
            sys.exit(1)

        print(f"Converting to MP3...")
        convert_to_mp3(wav_path, mp3_path)

    # 3. Tag
    title = frontmatter.get("title", slug)
    add_id3_tags(mp3_path, title=title)

    # 4. Update frontmatter
    audio_url = f"assets/audio/{slug}.mp3"
    if not args.skip_frontmatter_update:
        update_frontmatter(args.post, audio_url)
        print(f"Frontmatter updated: audio: \"{audio_url}\"")

    # 5. Report
    from mutagen.mp3 import MP3

    audio = MP3(str(mp3_path))
    duration = audio.info.length
    size_mb = mp3_path.stat().st_size / (1024 * 1024)
    print(f"Generated: {mp3_path}")
    print(f"Duration:  {int(duration // 60)}:{int(duration % 60):02d}")
    print(f"Size:      {size_mb:.1f} MB")


if __name__ == "__main__":
    main()
