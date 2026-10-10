---
layout: doc
title: "scry_ms_autosuggest_localized"
summary: "Modify the data passed from PHP to the front‑end autoSuggestLocalized object used by the autosuggest script."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Autosuggest"
---

Modify the data passed from PHP to the front‑end `autoSuggestLocalized` object used by the autosuggest script.


|               |                                                            |
| ------------- | ---------------------------------------------------------- |
| **Type**      | Filter                                                     |
| **Arguments** | `array $autosuggest_localized`                             |
| **Returns**   | `array`                                                    |
| **When**      | When autosuggest is enabled and its front‑end script is enqueued. |


Default keys include:

- `classSelector` — optional CSS class (token only) that limits which discovered forms get autosuggest; empty string means all discovered forms
- `restApiUrl` — REST URL for the autosuggest endpoint (`scry-search/v1/autosuggest`)

This is separate from [`scry_ms_window_localized`]({{ '/scry-search/filters/scry_ms_window_localized/' | relative_url }}) / `windowLocalized`. Use the window filter for form discovery (`searchFormSelectors`); use this filter for autosuggest-only config. Do not put admin API keys here — anything returned is exposed to the browser.

```php
add_filter( 'scry_ms_autosuggest_localized', function ( $data ) {
    $data['minChars'] = 2; // read in your own JS; core currently hard-codes 3
    return $data;
} );
```
