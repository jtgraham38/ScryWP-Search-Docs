---
layout: doc
title: "scry_ms_fa_excluded_taxonomies"
summary: "Filters taxonomy slugs excluded from the shortcode generator catalog (and any other call sites that use the helper)."
plugin: scry-search-filters
plugin_name: "Scry Search Filters"
plugin_url: "/scry-search-filters/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search-filters/filters/"
category: "Catalog"
---

Filters taxonomy slugs excluded from the shortcode generator catalog (and any other call sites that use the helper).

Prefer reading the list through `scry_ms_fa_get_excluded_taxonomies( $defaults )` so the filter always runs.

**Location:** `[includes/hooks-helpers.php](includes/hooks-helpers.php)`  
**Call site (current):** shortcode generator catalog in `[features/shortcode/feature.php](features/shortcode/feature.php)`

```php
add_filter( 'scry_ms_fa_excluded_taxonomies', function( $excluded ) {
    $excluded[] = 'product_visibility';
    return array_values( array_diff( $excluded, array( 'post_format' ) ) ); // re-enable one
} );
```


| Parameter              | Type    | Description                      |
| ---------------------- | ------- | -------------------------------- |
| `$excluded_taxonomies` | `array` | Default slugs from plugin config |


**Returns:** `array` of taxonomy slug strings.

**Helper:**

```php
$excluded = scry_ms_fa_get_excluded_taxonomies(
    array( 'post_format', 'nav_menu', 'link_category', 'wp_theme', 'wp_template_part_area' )
);
```
