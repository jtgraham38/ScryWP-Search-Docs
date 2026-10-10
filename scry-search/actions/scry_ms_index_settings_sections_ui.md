---
layout: doc
title: "scry_ms_index_settings_sections_ui"
summary: "Renders inside the per‑index settings dialog, allowing you to output custom settings UI."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: action
doc_type_label: "PHP action"
type_url: "/scry-search/actions/"
category: "Lifecycle"
---

Renders inside the per‑index settings dialog, allowing you to output custom settings UI.


|               |                                                     |
| ------------- | --------------------------------------------------- |
| **Type**      | Action                                              |
| **Arguments** | `array $index` (display data for the current index) |
| **When**      | While the index settings dialog is rendered.        |


Echo your own markup from the callback. `$index` includes display fields such as `name` (post type) and `index_name`.
