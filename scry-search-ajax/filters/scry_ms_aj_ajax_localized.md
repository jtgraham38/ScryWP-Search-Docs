---
layout: doc
title: "scry_ms_aj_ajax_localized"
summary: "Filters the data passed to wp_localize_script for the front-end shortcode script (scrySearchAjax)."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search-ajax/filters/"
category: "Ajax search"
---

Filters the data passed to `wp_localize_script` for the front-end shortcode script (`scrySearchAjax`).

| Arg | Type | Description |
|---|---|---|
| `$localized_data` | array | Script localization payload (endpoint URL, selectors, pagination defaults, etc.) |

**Returns:** `array`
