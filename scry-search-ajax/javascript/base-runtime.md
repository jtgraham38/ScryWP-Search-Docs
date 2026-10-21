---
layout: doc
title: "Base runtime"
heading: "Base runtime"
summary: "Pieces of window.scrySearch that this add-on uses."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: javascript
doc_type_label: "JavaScript API"
type_url: "/scry-search-ajax/javascript/"
category: "Runtime"
---

| Member | Description |
|---|---|
| `window.scrySearch` | Global runtime |
| `window.scrySearch.searchForms` | Registered `ScrySearch_SearchForm` instances |
| `window.scrySearch.upgrades` | Map of registered premium upgrades |
| `window.scrySearch.registerUpgrade(name, version)` | Reserve `upgrades[name]` (`name`, `version`, `data`) |
| `window.scrySearch.getSearchFormsByClass(className)` | Forms whose `<form>` has the given CSS class |
| `searchForm.submitAjax()` | Debounced AJAX submit; returns a `Promise` of the parsed JSON response |
| `searchForm.addPreSubmitAjaxAction(fn, order)` | Run before AJAX submit — `fn(searchForm)` |
| `searchForm.addPostSubmitAjaxAction(fn, order)` | Run after AJAX response — `fn(searchForm, data)` |
| `searchForm.data` | Per-form bag for upgrade state (e.g. `data.core`, `data.ajax`, `data.filters`) |
| `searchForm.ajaxEndpoint` | REST URL used by `submitAjax()` |

`scrySearchReady` is dispatched on **`document`** (not `window`). Listen there before touching the API.
