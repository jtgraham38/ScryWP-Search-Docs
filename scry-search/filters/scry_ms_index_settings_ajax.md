---
layout: doc
title: "scry_ms_index_settings_ajax"
summary: "Add or adjust the data returned to the index settings screen."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Index settings flow (per‑index configuration)"
---

Add or adjust the data returned to the index settings screen.


|               |                                                             |
| ------------- | ----------------------------------------------------------- |
| **Type**      | Filter                                                      |
| **Arguments** | `array $return_array`, `string $index_name`                 |
| **Returns**   | `array` — the response payload                              |
| **When**      | When current settings for an index are fetched for display. |


The payload includes keys such as `ranking_rules`, `searchable_attributes`, `available_fields`, `filterable_attributes`, `available_filterable_fields`, `synonyms`, `stop_words`, `dictionary`, and `typo_tolerance`. Add your own keys to surface custom data in companion UI.
