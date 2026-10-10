---
layout: doc
title: "Typical customization flow"
heading: "Typical customization flow"
summary: "Shortcode, custom Meilisearch filters, and generator catalog tips."
plugin: scry-search-filters
plugin_name: "Scry Search Filters"
plugin_url: "/scry-search-filters/"
doc_type: guide
doc_type_label: "Guide"
type_url: "/scry-search-filters/guides/"
category: "Guides"
---

### Shortcode / front end

1. Generate or hand-author `[scry-search-facets]` with escaped `groups` JSON
2. Optionally set `selector` so only specific Scry Search forms receive filters
3. Change the widget query selector globally via `scry_ms_fa_filters_localized`
4. Ensure Meilisearch indexes have the needed filterable attributes (e.g. `taxonomies.category.id`, `post_date_unix`)

### Custom Meilisearch filters

1. Submit extra fields from your own UI (or extend `groups`) under a consistent request shape
2. Translate them in `scry_ms_fa_search_filters`
3. Mirror anything worth reporting in `scry_ms_fa_analytics_filters_payload`

### Generator catalog

1. Adjust excluded taxonomies with `scry_ms_fa_excluded_taxonomies` so the admin Groups tab matches your site

---
