---
layout: doc
title: "Ajax action pipeline"
heading: "Ajax action pipeline"
summary: "Pre/post AJAX actions this add-on registers on each wrapped search form."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: javascript
doc_type_label: "JavaScript API"
type_url: "/scry-search-ajax/javascript/"
category: "Runtime"
---

| Pipeline | Order | Handler | Role |
|---|---|---|---|
| pre | `1` | `preparePaginationForSubmit` | Reset to page 1 unless `keepPage` |
| pre | `2` | `writeFederationToForm` | Inject `federation[…]` hidden fields |
| pre | `2` | `removeIsAutosuggestInput` | Strip base `is_autosuggest` input |
| pre | `2` | `showLoader` | Centered loader, or bottom infinite loader when appending |
| post | `10` | `removeFederationInputFields` | Clean federation hidden inputs |
| post | `10` | `hideLoader` | Hide both loaders |
| post | `50` | `displayStatReport` | Stats / “Showing X–Y of Z” |
| post | `60` | `updatePaginationUi` | Totals + paged button state |
| post | `100` | `displaySearchResults` | Paint / append HTML |

Lower `order` runs first. Custom code can insert around these with its own `order` values.
