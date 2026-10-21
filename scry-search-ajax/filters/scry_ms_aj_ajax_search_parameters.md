---
layout: doc
title: "scry_ms_aj_ajax_search_parameters"
summary: "Filters raw search parameters after they are read from the REST request, before the Meilisearch client runs."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search-ajax/filters/"
category: "Ajax search"
---

Filters raw search parameters after they are read from the REST request, before the Meilisearch client runs.

| Arg | Type | Description |
|---|---|---|
| `$params` | array | `[ $search_term, $post_types, $federation ]` |

**Returns:** `array` — same three-element shape; destructured back into `$search_term`, `$post_types`, `$federation`.
