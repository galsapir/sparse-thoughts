---
layout: page
title: Thoughts
---

<div class="tag-filters">
  <button class="tag-filter active" data-tag="all">all</button>
  {% assign all_tags = "" | split: "" %}
  {% for post in site.posts %}
    {% for tag in post.tags %}
      {% unless all_tags contains tag %}
        {% assign all_tags = all_tags | push: tag %}
      {% endunless %}
    {% endfor %}
  {% endfor %}
  {% assign all_tags = all_tags | sort %}
  {% for tag in all_tags %}
  <button class="tag-filter" data-tag="{{ tag }}">{{ tag }}</button>
  {% endfor %}
</div>

{% for post in site.posts %}
<p class="thought-item" data-tags="{{ post.tags | join: ' ' }}">
  <a href="{{ post.url | absolute_url }}">{{ post.title }}</a> <small>{{ post.date | date: "%b %d, %Y" }}</small>
  {% if post.tags.size > 0 %}
  <span class="post-tags">{{ post.tags | join: ", " }}</span>
  {% endif %}
</p>
{% endfor %}
