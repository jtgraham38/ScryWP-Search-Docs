---
layout: doc
title: "windowLocalized"
summary: "PHP-localized config object read by the front-end runtime."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: javascript
doc_type_label: "JavaScript API"
type_url: "/scry-search/javascript/"
category: "Runtime"
---

PHP exposes configuration to the runtime as the global `windowLocalized` object (modifiable with the [`scry_ms_window_localized`]({{ '/scry-search/filters/scry_ms_window_localized/' | relative_url }}) filter). Default keys include `restApiUrl`, `autoSuggestEnabled`, `searchFormSelectors`, `debounceMs` (AJAX debounce in milliseconds, default `250`), and `searchFormElementQuerySelector` (search input inside each form). Add your own keys server‑side to read them in your front‑end code.

Autosuggest uses a separate global, `autoSuggestLocalized` (modifiable with [`scry_ms_autosuggest_localized`]({{ '/scry-search/filters/scry_ms_autosuggest_localized/' | relative_url }})), so the two features do not overwrite each other. Default keys there are `classSelector` and `restApiUrl`.
