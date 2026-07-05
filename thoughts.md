---
layout: page
title: Thoughts
---

<div class="tag-filters">
  <button class="tag-filter active" data-tag="all">all</button>
  {% for tag in site.data.tags.vocabulary %}
  {% assign tagged = site.tags[tag.name] %}
  {% if tagged and tagged.size > 0 %}
  <button class="tag-filter" data-tag="{{ tag.name }}" data-description="{{ tag.description | escape }}">{{ tag.name }} <span class="tag-count">{{ tagged.size }}</span></button>
  {% endif %}
  {% endfor %}
</div>
<p class="tag-description" id="tag-description"></p>

{% for post in site.posts %}
<p class="thought-item" data-tags="{{ post.tags | join: ' ' }}">
  <a href="{{ post.url | absolute_url }}">{{ post.title }}</a> <small>{{ post.date | date: "%b %d, %Y" }}</small>
  {% if post.tags.size > 0 %}
  <span class="post-tags">{{ post.tags | join: ", " }}</span>
  {% endif %}
</p>
{% endfor %}
