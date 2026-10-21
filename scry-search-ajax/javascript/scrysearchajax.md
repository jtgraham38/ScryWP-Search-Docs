---
layout: doc
title: "scrySearchAjax"
summary: "Localized object for the Ajax shortcode script (filterable via scry_ms_aj_ajax_localized)."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: javascript
doc_type_label: "JavaScript API"
type_url: "/scry-search-ajax/javascript/"
category: "Runtime"
---

| Key | Default | Description |
|---|---|---|
| `search_term_param` | `'s'` | Search input name |
| `classSelector` | `'scry_ms_aj_search-form'` | Class used with `getSearchFormsByClass` |
| `ajaxSubmitEndpoint` | REST search URL | Assigned to `searchForm.ajaxEndpoint` |
| `resultsSectionElementQuerySelector` | `'.scry_ms_aj_results'` | Scrollable results panel |
| `resultsContainerElementQuerySelector` | `'.scry_ms_aj_results-container'` | Hits markup target |
| `statReportElementQuerySelector` | `'.scry_ms_aj_stat-report'` | “X results…” line |
| `loaderElementQuerySelector` | `'.scry_ms_aj_loader'` | Centered overlay spinner |
| `infiniteLoaderElementQuerySelector` | `'.scry_ms_aj_infinite-loader'` | Bottom spinner for infinite scroll |
| `paginationElementQuerySelector` | `'.scry_ms_aj_pagination'` | Paged controls `<nav>` |
| `paginationPagesQuerySelector` | `'.scry_ms_aj_pagination-pages'` | Numbered page buttons host |
| `pageSizeSelectQuerySelector` | `'[data-scry-aj-page-size]'` | Results-per-page `<select>` |
| `infiniteSentinelQuerySelector` | `'.scry_ms_aj_infinite-sentinel'` | Infinite-scroll sentinel |
| `hideElementClass` | `'scry_ms_aj_hidden'` | Utility class toggled on loaders |
| `nonePaginationLimit` | `1000` | `federation.limit` when `pagination="none"` |
