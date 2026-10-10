---
layout: doc
title: "scry_ms_index_searchable_attributes_before_update"
summary: "The array is already ordered from the Searchable Fields list (top to bottom) when this filter runs after a settings save."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Index settings flow (per‑index configuration)"
---

|               |                                                                                                                                                                        |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Type**      | Filter                                                                                                                                                                 |
| **Arguments** | `array $searchable_attributes`, `string $index_name`                                                                                                                   |
| **Returns**   | `array`                                                                                                                                                                |
| **When**      | Before searchable attributes are applied to an index — both when settings are saved and when an index's searchable attributes are configured (e.g. on index creation). |


The array is already ordered from the Searchable Fields list (top to bottom) when this filter runs after a settings save.

```php
add_filter( 'scry_ms_index_searchable_attributes_before_update', function ( $attributes, $index_name ) {
    $attributes[] = 'reading_time';
    return $attributes;
}, 10, 2 );
```
