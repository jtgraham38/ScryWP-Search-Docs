---
layout: list
title: "Guides — Scry Search Filters"
summary: "Concepts and setup notes for Scry Search Filters."
plugin: scry-search-filters
plugin_name: "Scry Search Filters"
plugin_url: "/scry-search-filters/"
doc_type: guide
doc_type_label: "Guide"
list_kind: type
show_filter_search: false
---

### Basics

| Name | Summary |
| ---- | ------- |
| [Filters upgrade overview]({{ '/scry-search-filters/guides/overview/' | relative_url }}) | Public extension points for Scry Search: Meilisearch Filtered Search. All add-on hooks use the scry_ms_fa_ prefix. |

### Guides

| Name | Summary |
| ---- | ------- |
| [Notes & unsupported surfaces]({{ '/scry-search-filters/guides/notes/' | relative_url }}) | These are hooks fired by this add-on. The plugin also consumes base Scry Search hooks prefixed scry_ms_ (see README.md) — e.g. scry_ms_multi_search_query, scry_ms_analytics_event_to_insert, scry_ms_premium_upgrade_settin… |
| [Typical customization flow]({{ '/scry-search-filters/guides/customization-flow/' | relative_url }}) | Shortcode, custom Meilisearch filters, and generator catalog tips. |

### Search

| Name | Summary |
| ---- | ------- |
| [Built-in filter construction]({{ '/scry-search-filters/guides/built-in-filter-construction/' | relative_url }}) | Location: ScrySearch_Filters_SearchFeature::add_filters_to_search_query() in features/search/feature.php Hooked to: base plugin scry_ms_multi_search_query (per index). |

