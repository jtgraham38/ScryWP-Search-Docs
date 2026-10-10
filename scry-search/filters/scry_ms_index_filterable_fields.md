---
layout: doc
title: "scry_ms_index_filterable_fields"
summary: "Modify the list of fields offered for a post type in the filterable fields tree."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Indexing & document shaping"
---

Modify the list of fields offered for a post type in the **filterable** fields tree.


|               |                                                                            |
| ------------- | -------------------------------------------------------------------------- |
| **Type**      | Filter                                                                     |
| **Arguments** | `array $fields`, `string $post_type`                                       |
| **Returns**   | `array` — the fields map                                                   |
| **When**      | When the configuration UI builds the filterable field list for a post type.|


Same shape as `scry_ms_index_fields`. Taxonomy entries typically use paths like `taxonomies.<taxonomy>.id`.
