---
layout: doc
title: "scry_ms_analytics_recent_searches_columns"
summary: "Add, remove, or reorder columns on the Search Analytics Recent Searches table."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Analytics"
---

Add, remove, or reorder columns on the Search Analytics **Recent Searches** table.


|               |                                                                 |
| ------------- | --------------------------------------------------------------- |
| **Type**      | Filter                                                          |
| **Arguments** | `array $columns` (map of column slug => heading label)          |
| **Returns**   | `array`                                                         |
| **When**      | When the Recent Searches `WP_List_Table` builds its headers.    |


Default keys: `search_term`, `user`, `user_ip`, `result_count`, `is_autosuggest`, `created_at`. Pair this with `scry_ms_analytics_recent_searches_column` to render added columns. Extra event data from `scry_ms_analytics_event_to_insert` is available on each row as a decoded `search_metadata` array.

```php
add_filter( 'scry_ms_analytics_recent_searches_columns', function ( $columns ) {
    $columns['filters'] = __( 'Filters', 'my-plugin' );
    return $columns;
} );
```
