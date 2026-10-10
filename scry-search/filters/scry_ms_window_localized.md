---
layout: doc
title: "scry_ms_window_localized"
summary: "Modify the data passed from PHP to the front‑end windowLocalized object used by the JavaScript runtime."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Front‑end window localization"
---

Modify the data passed from PHP to the front‑end `windowLocalized` object used by the JavaScript runtime.


|               |                                               |
| ------------- | --------------------------------------------- |
| **Type**      | Filter                                        |
| **Arguments** | `array $window_localized`                     |
| **Returns**   | `array`                                       |
| **When**      | When the front‑end window script is enqueued. |


Default keys include:

- `restApiUrl` — REST URL used by form AJAX submits (autosuggest endpoint by default)
- `autoSuggestEnabled` — whether autosuggest is enabled in settings
- `searchFormSelectors` — **array of CSS selectors** used to discover `<form>` elements on the page
- `debounceMs` — milliseconds `submitAjax()` waits after the last call before sending (default `250`). Read as `windowLocalized.debounceMs`.

Use this filter to add discovery selectors for custom theme or builder search forms (see [Form discovery]({{ '/scry-search/javascript/form-discovery/' | relative_url }}) below), or to change the AJAX debounce.

```php
add_filter( 'scry_ms_window_localized', function ( $data ) {
    $data['debounceMs'] = 400;
    return $data;
} );
```

```php
add_filter( 'scry_ms_window_localized', function ( $data ) {
    if ( empty( $data['searchFormSelectors'] ) || ! is_array( $data['searchFormSelectors'] ) ) {
        $data['searchFormSelectors'] = array();
    }
    // Match any <form> that carries this class.
    $data['searchFormSelectors'][] = 'form.my-site-search';
    // Or match a Gutenberg-style block form.
    $data['searchFormSelectors'][] = 'form.wp-block-search';
    return $data;
} );
```
