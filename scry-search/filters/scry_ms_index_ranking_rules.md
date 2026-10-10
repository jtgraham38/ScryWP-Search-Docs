---
layout: doc
title: "scry_ms_index_ranking_rules"
summary: "Change the default Meilisearch ranking rules."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Indexing & document shaping"
---

Change the default Meilisearch ranking rules.


|               |                                                     |
| ------------- | --------------------------------------------------- |
| **Type**      | Filter                                              |
| **Arguments** | `array $ranking_rules` (ordered list of rule names) |
| **Returns**   | `array` — the ranking rules                         |
| **When**      | When default ranking rules are resolved.            |


Order matters: rules are applied top to bottom.
