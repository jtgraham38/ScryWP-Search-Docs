---
layout: doc
title: "scry_ms_should_insert_analytics_event"
summary: "Decide whether a prepared analytics event is written to the database."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Analytics"
---

Decide whether a prepared analytics event is written to the database.


|               |                                                                 |
| ------------- | --------------------------------------------------------------- |
| **Type**      | Filter                                                          |
| **Arguments** | `bool $should_insert`, `array $event_to_insert`                 |
| **Returns**   | `bool` — `true` to insert, `false` to skip                      |
| **When**      | After `scry_ms_analytics_event_to_insert` and metadata packing, immediately before the database insert. |


The default is `true`. `$event_to_insert` is the packed row (table columns plus `search_metadata` JSON). Returning `false` skips the insert and `insert_search_analytics_event()` returns `false`.

```php
add_filter( 'scry_ms_should_insert_analytics_event', function ( $should_insert, $event ) {
    if ( strlen( $event['search_term'] ) < 3 ) {
        return false;
    }
    return $should_insert;
}, 10, 2 );
```
