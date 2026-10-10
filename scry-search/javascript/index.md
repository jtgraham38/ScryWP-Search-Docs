---
layout: list
title: "JavaScript API — Scry Search"
summary: "Runtime and front-end API pages for Scry Search."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: javascript
doc_type_label: "JavaScript API"
list_kind: type
show_filter_search: false
---

### Runtime

| Name | Summary |
| ---- | ------- |
| [Form discovery]({{ '/scry-search/javascript/form-discovery/' | relative_url }}) | How the runtime finds <form> elements and wraps them as ScrySearch_SearchForm instances. |
| [JavaScript runtime overview]({{ '/scry-search/javascript/overview/' | relative_url }}) | The plugin ships a small front‑end runtime, window.scrySearch, that discovers search forms on the page and gives you ordered hooks to run code before/after a search — both for normal submits and AJAX submits (used by aut… |
| [ScrySearch_SearchForm]({{ '/scry-search/javascript/scrysearch-searchform/' | relative_url }}) | Per-form wrapper with submit/submitAjax and ordered pre/post action hooks. |
| [scrySearchReady]({{ '/scry-search/javascript/scrysearchready/' | relative_url }}) | Event dispatched on document after forms are discovered — wait for this before using the API. |
| [Submit action pipeline]({{ '/scry-search/javascript/submit-action-pipeline/' | relative_url }}) | Ordered pre/post actions for normal and AJAX submits. |
| [Upgrades]({{ '/scry-search/javascript/upgrades/' | relative_url }}) | Reserve a namespace on window.scrySearch.upgrades for premium add-ons. |
| [window.scrySearch]({{ '/scry-search/javascript/window-scrysearch/' | relative_url }}) | Global runtime object: version, form getters, and registerUpgrade(). |
| [windowLocalized]({{ '/scry-search/javascript/windowlocalized/' | relative_url }}) | PHP-localized config object read by the front-end runtime. |

