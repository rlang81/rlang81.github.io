---
layout: page
title: Photography
---

## April 8th Total Solar Eclipse

![HDR Composite](https://rlang81.github.io/assets/img/photography/maine-tse-2024/hdr-stack-1.png) ![View from the Rangeley, ME IGA](https://rlang81.github.io/assets/img/photography/maine-tse-2024/PXL_20240408_193142221.jpg)

{% assign images = site.static_files | where: "gallery", true %}
<ul>
  {% for img in images %}
    <li><a href="{{ img.path }}" title="{{ img.basename }}" class="img">{{ img.basename }}</a></li>
  {% endfor %}
</ul>
