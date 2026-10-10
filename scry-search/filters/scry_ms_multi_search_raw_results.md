---
layout: doc
title: "scry_ms_multi_search_raw_results"
summary: "Inspect, filter, or reorder the raw hits returned by Meilisearch before they are resolved into posts."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Search query (front‑end search interception)"
---

Inspect, filter, or reorder the raw hits returned by Meilisearch before they are resolved into posts.


|               |                                                                              |
| ------------- | ---------------------------------------------------------------------------- |
| **Type**      | Filter                                                                       |
| **Arguments** | `array $all_results` (list of raw hit documents)                             |
| **Returns**   | `array` — the (possibly modified) list of hits                               |
| **When**      | Immediately after the search response is received, before posts are fetched. |


> **Note:** the total result count is derived from the array you return (`count($all_results)`), so adding or removing hits here also adjusts the reported total.

```php
add_filter( 'scry_ms_multi_search_raw_results', function ( $all_results ) {
    // e.g. drop hits that fail a custom check
    return array_values( array_filter( $all_results, 'my_keep_hit' ) );
} );
```
