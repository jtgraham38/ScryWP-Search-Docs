---
layout: doc
title: "scry_ms_fa_filters_localized"
summary: "Filters the array passed to wp_localize_script as scrySearchFilters for the front-end filters script."
plugin: scry-search-filters
plugin_name: "Scry Search Filters"
plugin_url: "/scry-search-filters/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search-filters/filters/"
category: "Shortcode"
---

Filters the array passed to `wp_localize_script` as `scrySearchFilters` for the front-end filters script.

**Location:** `ScrySearch_Filters_ShortcodeFeature::filters_scripts()` in `[features/shortcode/feature.php](features/shortcode/feature.php)`

```php
add_filter( 'scry_ms_fa_filters_localized', function( $data ) {
    // Match widgets that use a custom class instead of form.scry-search-facets.
    $data['selector'] = '.my-site-filters, form.scry-search-facets';
    return $data;
} );
```


| Parameter         | Type    | Description                                                 |
| ----------------- | ------- | ----------------------------------------------------------- |
| `$localized_data` | `array` | Default includes `selector` => `'form.scry-search-facets'` |


**Returns:** `array` localized for `scrySearchFilters` in JS.
