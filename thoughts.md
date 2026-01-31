---
layout: page
title: Thoughts
---

{% for post in site.posts %}
<p>
  <a href="{{ post.url | absolute_url }}">{{ post.title }}</a> <small>{{ post.date | date: "%b %d, %Y" }}</small>
</p>
{% endfor %}
