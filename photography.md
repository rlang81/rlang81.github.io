---
layout: page
title: Photography
---

<style>
  .gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }

  .gallery-item {
    flex-basis: calc(33.33% - 10px); /* Adjust width for three columns with spacing */
    margin-bottom: 20px; /* Adjust spacing between rows */
  }

  .gallery-item img {
    width: 100%; /* Ensure images fill their container */
    height: auto; /* Maintain aspect ratio */
  }
</style>



{% assign images = site.static_files | where: "gallery", true %}
<div class="gallery">
  {% for img in images %}
    {% assign thumbnail_path = img.path | replace: "/photography/", "/thumbnails/photography/" %}
    <a href="{{ img.path }}" title="{{ img.basename }}" class="gallery-item">
      <img src="{{ thumbnail_path }}" alt="{{ img.basename }}">
    </a>
  {% endfor %}
</div>
