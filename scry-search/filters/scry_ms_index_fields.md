---
layout: doc
title: "scry_ms_index_fields"
summary: "Modify the list of fields offered for a post type in the index configuration UI (searchable fields tree)."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Indexing & document shaping"
---

Modify the list of fields offered for a post type in the index configuration UI (searchable fields tree).


|               |                                                                  |
| ------------- | ---------------------------------------------------------------- |
| **Type**      | Filter                                                           |
| **Arguments** | `array $fields`, `string $post_type`                             |
| **Returns**   | `array` — the fields map                                         |
| **When**      | When the configuration UI builds the field list for a post type. |


Each entry is keyed by field path and contains at least `label`, `type`, and `path`.
