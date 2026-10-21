---
layout: doc
title: "scry_ms_aj_ajax_search_federation"
summary: "Filters the Meilisearch\\Contracts\\MultiSearchFederation object (limit/offset, and any further federation options you attach)."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search-ajax/filters/"
category: "Ajax search"
---

Filters the `Meilisearch\Contracts\MultiSearchFederation` object (limit/offset, and any further federation options you attach).

| Arg | Type | Description |
|---|---|---|
| `$federation_options` | `MultiSearchFederation` | Federation options sent to `multiSearch` |
| `$post_types` | array | Requested post types |
| `$federation` | array | Sanitized federation request array |

**Returns:** `MultiSearchFederation`
