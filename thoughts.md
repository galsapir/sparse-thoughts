---
layout: page
title: Thoughts
---

{% for post in site.posts %}
<p>
  <span class="post-date">{{ post.date | date: "%b %d, %Y" }}</span> — <a href="{{ post.url | absolute_url }}">{{ post.title }}</a>
</p>
{% endfor %}
