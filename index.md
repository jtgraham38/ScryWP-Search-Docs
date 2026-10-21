---
layout: default
title: Welcome
summary: Developer documentation for Scry Search and premium upgrades.
show_sidebar: true
---

<section class="hero">
  <p class="eyebrow">Developer reference</p>
  <h1>Scry Search Docs</h1>
  <p>
    One page per hook and runtime surface for the open-source
    <a href="https://wordpress.org/plugins/scry-search/">Scry Search</a> plugin
    and its premium upgrades. Hosted Meilisearch lives at
    <a href="https://scrywp.com/">scrywp.com</a>.
  </p>
  <div class="hero-actions">
    <a class="btn btn-primary" href="{{ '/scry-search/' | relative_url }}">Scry Search</a>
    <a class="btn btn-ghost" href="{{ '/scry-search-filters/' | relative_url }}">Filters</a>
    <a class="btn btn-ghost" href="{{ '/scry-search-ajax/' | relative_url }}">Ajax</a>
    <a class="btn btn-ghost" href="{{ '/reference/' | relative_url }}">Browse everything</a>
  </div>
</section>

<div class="plugin-grid">
  <article class="plugin-card">
    <span class="badge">Core plugin</span>
    <h2>Scry Search</h2>
    <p>Meilisearch-powered WordPress search. PHP filters &amp; actions (<code>scry_ms_*</code>) plus the <code>window.scrySearch</code> runtime.</p>
    <div class="meta">
      <span class="badge type-filter">43 filters</span>
      <span class="badge type-action">7 actions</span>
      <span class="badge type-javascript">8 JS pages</span>
    </div>
    <a class="btn btn-primary" href="{{ '/scry-search/' | relative_url }}">Open docs</a>
  </article>

  <article class="plugin-card">
    <span class="badge">Premium upgrade</span>
    <h2>Scry Search Filters</h2>
    <p>Faceted filtering via <code>[scry-search-facets]</code>, Meilisearch filter assembly, analytics payloads, and a <code>window.scrySearch</code> upgrade (<code>scry_ms_fa_*</code>).</p>
    <div class="meta">
      <span class="badge type-filter">5 filters</span>
      <span class="badge type-shortcode">1 shortcodes</span>
      <span class="badge type-javascript">1 JS pages</span>
    </div>
    <a class="btn btn-primary" href="{{ '/scry-search-filters/' | relative_url }}">Open docs</a>
  </article>

  <article class="plugin-card">
    <span class="badge">Premium upgrade</span>
    <h2>Scry Search Ajax</h2>
    <p>In-place results via <code>[scry-search-ajax]</code>, a public REST search route, and a <code>window.scrySearch</code> upgrade (<code>scry_ms_aj_*</code>).</p>
    <div class="meta">
      <span class="badge type-filter">9 filters</span>
      <span class="badge type-rest">1 REST</span>
      <span class="badge type-javascript">7 JS pages</span>
    </div>
    <a class="btn btn-primary" href="{{ '/scry-search-ajax/' | relative_url }}">Open docs</a>
  </article>
</div>

<section class="section-block" style="margin-top:2.5rem">
  <h2>How this repo is organized</h2>
  <p>Each plugin has its own tree. Inside a plugin, pages are grouped by type (guides, REST, PHP filters, PHP actions, shortcodes, JavaScript API). Future upgrades can add another top-level folder the same way.</p>
</section>
