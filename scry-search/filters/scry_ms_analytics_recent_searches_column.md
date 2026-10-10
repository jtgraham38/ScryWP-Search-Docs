---
layout: doc
title: "scry_ms_analytics_recent_searches_column"
summary: "Render a custom Recent Searches column cell (or override the default HTML for a slug that has no dedicated column_* method)."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Analytics"
---

Render a custom Recent Searches column cell (or override the default HTML for a slug that has no dedicated `column_*` method).


|               |                                                                 |
| ------------- | --------------------------------------------------------------- |
| **Type**      | Filter                                                          |
| **Arguments** | `string $output`, `array $item`, `string $column_name`          |
| **Returns**   | `string` — HTML for the cell                                    |
| **When**      | For each cell that falls through `column_default`.              |


`$item` is one analytics row (decoded JSON fields plus `search_metadata`). Return already-escaped HTML.

```php
add_filter( 'scry_ms_analytics_recent_searches_column', function ( $output, $item, $column_name ) {
    if ( 'filters' !== $column_name ) {
        return $output;
    }
    $metadata = isset( $item['search_metadata'] ) && is_array( $item['search_metadata'] )
        ? $item['search_metadata']
        : array();
    if ( empty( $metadata['scry_search_filters'] ) ) {
        return '&mdash;';
    }
    return esc_html( wp_json_encode( $metadata['scry_search_filters'] ) );
}, 10, 3 );
```

Optional: `scry_ms_analytics_recent_searches_sortable_columns` receives the sortable map (`slug => array( orderby, is_default_desc )`). Only slugs that match real SQL columns on the analytics table will sort correctly.
