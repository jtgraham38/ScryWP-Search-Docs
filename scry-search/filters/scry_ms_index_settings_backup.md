---
layout: doc
title: "scry_ms_index_settings_backup"
summary: "Modify the settings payload that is persisted locally when an index is saved."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Index settings flow (per‑index configuration)"
---

Modify the settings payload that is persisted locally when an index is saved.


|               |                                                      |
| ------------- | ---------------------------------------------------- |
| **Type**      | Filter                                               |
| **Arguments** | `array $index_settings_backup`, `string $index_name` |
| **Returns**   | `array` — the payload to persist                     |
| **When**      | Right before the settings backup is saved.           |


`$index_settings_backup` contains: `ranking_rules`, `searchable_attributes`, `synonyms`, `stop_words`, `filterable_attributes`, `dictionary`, `typo_tolerance`, `hybrid` (enabled, embedder, semantic_ratio, and embedders map for restore).

---

The following filters fire **immediately before** each setting group is applied to Meilisearch. Each receives the index name as a second argument and must return the (possibly modified) value.
