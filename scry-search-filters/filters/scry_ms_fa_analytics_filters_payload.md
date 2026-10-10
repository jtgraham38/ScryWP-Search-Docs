---
layout: doc
title: "scry_ms_fa_analytics_filters_payload"
summary: "Filters the analytics extras payload attached as scry_search_filters on the base plugin analytics event."
plugin: scry-search-filters
plugin_name: "Scry Search Filters"
plugin_url: "/scry-search-filters/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search-filters/filters/"
category: "Analytics"
---

Filters the analytics extras payload attached as `scry_search_filters` on the base plugin analytics event.

Return an empty array to omit the key entirely.

Default payload shape when filters were applied:

```php
array(
    'general' => array(
        'type' => 'post', // or list of slugs; from facets general.type or top-level post_type
        'publishDate' => array( 'from' => '2024-01-01', 'to' => '2024-06-01' ),
    ),
    'taxonomies' => array(
        'category' => array(
            array( 'id' => 12, 'name' => 'News', 'slug' => 'news' ),
        ),
    ),
)
```

**Location:** `ScrySearch_Filters_AnalyticsFeature::build_analytics_filters_payload()` in `[features/analytics/feature.php](features/analytics/feature.php)`

```php
add_filter( 'scry_ms_fa_analytics_filters_payload', function( $payload, $facets ) {
    if ( ! empty( $facets['custom'] ) ) {
        $payload['custom'] = $facets['custom'];
    }
    return $payload;
}, 10, 2 );
```


| Parameter  | Type    | Description                                |
| ---------- | ------- | ------------------------------------------ |
| `$payload` | `array` | Built analytics filters payload            |
| `$facets`  | `array` | Raw `scry-search[facets]` from the request |


**Returns:** `array` payload. Non-arrays become `[]` (key omitted when empty).

Supports both the current slug-based taxonomy map and a legacy term-ID list under `taxonomies`.
