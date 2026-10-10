---
layout: doc
title: "scry_ms_index_settings_restore"
summary: "Fires after a saved settings backup is re‑applied to an index."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: action
doc_type_label: "PHP action"
type_url: "/scry-search/actions/"
category: "Lifecycle"
---

Fires after a saved settings backup is re‑applied to an index.


|               |                                                                            |
| ------------- | -------------------------------------------------------------------------- |
| **Type**      | Action                                                                     |
| **Arguments** | `object $index` (Meilisearch index handle), `array $index_settings_backup` |
| **When**      | After previously saved settings are restored onto an index.                |


`$index_settings_backup` has the same shape as the `scry_ms_index_settings_backup` filter (`ranking_rules`, `searchable_attributes`, `synonyms`, `stop_words`, `filterable_attributes`, `dictionary`, `typo_tolerance`, `hybrid`).
