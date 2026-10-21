---
layout: doc
title: "ScrySearchAjax_SearchForm"
summary: "Per-form controller for pagination, federation hidden inputs, and results rendering."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: javascript
doc_type_label: "JavaScript API"
type_url: "/scry-search-ajax/javascript/"
category: "Runtime"
---

Controller constructed per ajax shortcode form. Notable instance state:

| Member | Description |
|---|---|
| `searchForm` | Wrapped base `ScrySearch_SearchForm` |
| `formElement` | The `<form>` |
| `wrapperElement` | Shortcode root (reads `data-pagination`, `data-page-size`) |
| `paginationMode` | `'none'` \| `'paged'` \| `'infinite'` |
| `pageSize` | Hits per page |
| `federation` | `{ limit, offset, page, hitsPerPage, facetsByIndex, mergeFacets }` written as hidden inputs on submit |
| `keepPage` / `appendResults` | Flags for pagination vs fresh search |
| `totalHits` / `totalPages` | From last response’s `estimatedTotalHits` |
| `loadingMore` | Guards concurrent infinite-scroll fetches |

Important methods:

| Method | Description |
|---|---|
| `goToPage(page, appendResults)` | Sets `keepPage`, optional append, syncs federation, calls `submitAjax()` |
| `maybeLoadNextInfinitePage()` | Loads next page when the results panel is near its bottom |
| `syncFederationFromPage()` | Derives `limit` / `offset` from `page` + `pageSize` |
| `writeFederationToForm()` | Appends `federation[…]` hidden inputs before AJAX |
| `displaySearchResults(searchForm, results)` | Replaces or appends `results.rendered` |
| `displayStatReport(searchForm, results)` | Updates the stats line (range text when paginated) |

On construct it also:

1. Sets `searchForm.data.core.shouldRenderAutosuggest = false` (disables base autosuggest UI for this form).
2. Points `searchForm.ajaxEndpoint` at `scrySearchAjax.ajaxSubmitEndpoint`.
3. Registers the pre/post AJAX actions below.
4. Binds paged controls and infinite scroll when applicable.
5. If facets are attached (`searchForm.data.filters.filtersForms`), listens for `scrySearchFiltersFacetChange` and re-runs `submitAjax()` when the query is non-empty.
