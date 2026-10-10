---
layout: doc
title: "scry_ms_analytics_event_to_insert"
summary: "Modify a search analytics record before it is stored."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Analytics"
---

Modify a search analytics record before it is stored.


|               |                                         |
| ------------- | --------------------------------------- |
| **Type**      | Filter                                  |
| **Arguments** | `array $event_to_insert`                |
| **Returns**   | `array` — the record to store           |
| **When**      | Before each analytics event is written. |


Keys include: `search_term`, `user_id`, `user_ip`, `user_agent`, `referrer`, `result_count`, `result_ids`, `result_titles`, `post_types_searched`, `is_autosuggest`. Use this to further anonymize data, or to attach premium-plugin payloads.

`is_autosuggest` is `0` unless the insert payload sets it (the hidden field autosuggest adds before its AJAX search).

**Core hybrid tracking (1.5+):** when federated search uses hybrid on any index, the analytics feature adds `scry_search_hybrid` with per-index `embedder` and `semantic_ratio` before this filter runs.

**Premium / extra fields:** add a top-level key named for your plugin (for example `scry_search_filters`). After this filter runs, any keys that are not table columns are packed into the `search_metadata` JSON column and stored with the event. You may also set a `search_metadata` array directly; it is merged with those packed keys. Omit your key when you have nothing to report.
