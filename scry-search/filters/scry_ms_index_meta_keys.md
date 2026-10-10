---
layout: doc
title: "scry_ms_index_meta_keys"
summary: "Modify the list of post‑meta keys discovered for a post type."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Indexing & document shaping"
---

Modify the list of post‑meta keys discovered for a post type.


|               |                                                                             |
| ------------- | --------------------------------------------------------------------------- |
| **Type**      | Filter                                                                      |
| **Arguments** | `array $meta_keys` (list of meta key strings), `string $post_type`          |
| **Returns**   | `array` — the meta key list                                                 |
| **When**      | When meta keys are gathered for a post type (used to build the field list). |


Use this to expose meta keys that wouldn't otherwise be discovered, or to hide private ones.
