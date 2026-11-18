// ABOUTME: Implements interactive controls on Sparse Thoughts.
// ABOUTME: Handles themes, post copying, and navigation filters.
(function(document) {
  // Theme toggle
  var themeToggle = document.querySelector('.theme-toggle');
  var html = document.documentElement;

  // Check for saved preference, then system preference
  var savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    html.setAttribute('data-theme', savedTheme);
  } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    html.setAttribute('data-theme', 'dark');
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', function() {
      var currentTheme = html.getAttribute('data-theme');
      var newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
    });
  }

  // Listen for system theme changes
  if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
      if (!localStorage.getItem('theme')) {
        html.setAttribute('data-theme', e.matches ? 'dark' : 'light');
      }
    });
  }

  /** @param {string} markdown @param {string} postUrl @returns {string} */
  function portablePostMarkdown(markdown, postUrl) {
    var fencedCode = /^ {0,3}(?<fence>(?<marker>[`~])\k<marker>{2,})[^\n]*\n[\s\S]*?(?:^ {0,3}\k<fence>\k<marker>*[ \t]*$|(?![\s\S]))/;
    var inlineCode = /(?<ticks>`+)[\s\S]*?(?<!`)\k<ticks>(?!`)/;
    var link = /(?<prefix>\]\(\s*|^ {0,3}\[(?!\^)[^\]\n]+\]:[ \t]*)(?:<(?<angled>[^<>\n]+)>|(?<plain>[^\s<>)]+))/;
    var tokens = new RegExp([fencedCode.source, inlineCode.source, link.source].join('|'), 'gm');

    return markdown.replace(tokens, function(match, ...parts) {
      var groups = parts[parts.length - 1];
      var destination = groups.angled || groups.plain;
      if (!destination || /^(#|[a-z][a-z\d+.-]*:)/i.test(destination)) return match;

      try {
        var absolute = new URL(destination, postUrl).href;
        return groups.prefix + (groups.angled ? '<' + absolute + '>' : absolute);
      } catch (error) {
        return match;
      }
    });
  }

  /** @param {string} value @returns {string} */
  function bibtexField(value) {
    var escapes = { '\\': '\\textbackslash{}', '~': '\\textasciitilde{}', '^': '\\textasciicircum{}' };
    return value.replace(/[\\{}$&#%_~^]/g, function(character) {
      return escapes[character] || '\\' + character;
    });
  }

  /** @param {HTMLElement} actions @param {string} format @returns {string} */
  function postCopyText(actions, format) {
    var post = actions.dataset;
    if (format === 'citation') {
      return `${post.author}. “${post.title}” ${post.siteName}, ${post.dateLabel}. ${post.url}`;
    }
    if (format === 'bibtex') {
      return [
        `@misc{${post.citeKey},`,
        `  author = {${bibtexField(post.author)}},`,
        `  title = {{${bibtexField(post.title)}}},`,
        `  howpublished = {${bibtexField(post.siteName)}},`,
        `  year = {${post.date.slice(0, 4)}},`,
        `  url = {${post.url}}`,
        '}'
      ].join('\n');
    }

    var source = actions.querySelector('[data-post-markdown]').content.textContent;
    return `# ${post.title}\n\n${post.author} · ${post.dateLabel} · ${post.url}\n\n${portablePostMarkdown(source, post.url)}\n`;
  }

  var postActions = document.querySelector('.post-actions');
  if (postActions) {
    var status = postActions.querySelector('[role="status"]');
    var copyText = postActions.querySelector('.post-copy-text');
    postActions.querySelectorAll('[data-copy]').forEach(function(button) {
      button.addEventListener('click', async function() {
        var text = postCopyText(postActions, button.dataset.copy);
        status.textContent = '';
        copyText.hidden = true;
        try {
          await navigator.clipboard.writeText(text);
          status.textContent = 'Copied.';
        } catch (error) {
          copyText.value = text;
          copyText.hidden = false;
          status.textContent = 'Copy the selected text.';
          copyText.focus();
          copyText.select();
        }
      });
    });
    postActions.hidden = false;
  }

  // "Show more" on homepage
  var showMoreBtn = document.getElementById('show-more-btn');
  if (showMoreBtn) {
    showMoreBtn.addEventListener('click', function() {
      var hidden = document.querySelectorAll('.post-hidden');
      for (var i = 0; i < hidden.length; i++) {
        hidden[i].classList.remove('post-hidden');
      }
      showMoreBtn.parentElement.remove();
    });
  }

  // Tag filtering on thoughts page; filter state lives in the URL hash so tags are linkable
  var tagFilters = document.querySelectorAll('.tag-filter');
  if (tagFilters.length > 0) {
    var items = document.querySelectorAll('.thought-item');
    var description = document.getElementById('tag-description');

    var applyFilter = function(tag) {
      var activeBtn = null;
      tagFilters.forEach(function(b) {
        b.classList.remove('active');
        if (b.getAttribute('data-tag') === tag) {
          activeBtn = b;
        }
      });
      if (!activeBtn) {
        tag = 'all';
        activeBtn = tagFilters[0];
      }
      activeBtn.classList.add('active');

      if (description) {
        description.textContent = activeBtn.getAttribute('data-description') || '';
      }

      items.forEach(function(item) {
        if (tag === 'all' || item.getAttribute('data-tags').split(' ').indexOf(tag) !== -1) {
          item.classList.remove('filtered-out');
        } else {
          item.classList.add('filtered-out');
        }
      });
      return tag;
    };

    tagFilters.forEach(function(btn) {
      btn.addEventListener('click', function() {
        var tag = applyFilter(btn.getAttribute('data-tag'));
        history.replaceState(null, '', tag === 'all' ? location.pathname : '#' + tag);
      });
    });

    if (location.hash.length > 1) {
      applyFilter(decodeURIComponent(location.hash.slice(1)));
    }
  }
})(document);
