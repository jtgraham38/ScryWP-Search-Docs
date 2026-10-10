---
layout: doc
title: "scry_ms_index_searchable_attributes"
summary: "Change the default searchable attributes list used when configuring new indexes."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Indexing & document shaping"
---

Change the **default** searchable attributes list used when configuring new indexes.


|               |                                                                                          |
| ------------- | ---------------------------------------------------------------------------------------- |
| **Type**      | Filter                                                                                   |
| **Arguments** | `array $searchable_attributes`                                                           |
| **Returns**   | `array` — attribute name list                                                            |
| **When**      | When default searchable attributes are resolved (distinct from `*_before_update` hooks). |


Prefer this when aligning defaults with custom document fields. Use `scry_ms_index_searchable_attributes_before_update` when mutating attributes at apply-time for a specific index.

The Index Settings UI lets you drag searchable fields to set their order. On save, checked attributes are sent to Meilisearch as `searchableAttributes` in that list order. Earlier entries are more important under the `attribute` / `attributeRank` ranking rule. When Meilisearch returns `["*"]` (all fields searchable), the UI expands that to every available field path so checkboxes match reality.
