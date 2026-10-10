---
layout: doc
title: "scry_ms_fa_analytics_recent_searches_filters_html"
summary: "Filters the HTML for the Filters column in the base plugin Recent Searches table."
plugin: scry-search-filters
plugin_name: "Scry Search Filters"
plugin_url: "/scry-search-filters/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search-filters/filters/"
category: "Analytics"
---

Filters the HTML for the **Filters** column in the base plugin Recent Searches table.

**Location:** `ScrySearch_Filters_AnalyticsFeature::render_recent_searches_column()` in `[features/analytics/feature.php](features/analytics/feature.php)`

```php
add_filter( 'scry_ms_fa_analytics_recent_searches_filters_html', function( $html, $filters, $item ) {
    // $filters is the stored scry_search_filters payload from search_metadata.
    return $html;
}, 10, 3 );
```


| Parameter  | Type     | Description                                            |
| ---------- | -------- | ------------------------------------------------------ |
| `$html`    | `string` | Default expandable dropdown cell markup                |
| `$filters` | `array`  | `scry_search_filters` from the row’s `search_metadata` |
| `$item`    | `array`  | Full analytics table row                               |


**Returns:** `string` HTML. Non-strings become `&mdash;`.
