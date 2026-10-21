---
layout: list
title: "JavaScript API — Scry Search Ajax"
summary: "Runtime and front-end API pages for Scry Search Ajax."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: javascript
doc_type_label: "JavaScript API"
list_kind: type
show_filter_search: false
---

### Runtime

| Name | Summary |
| ---- | ------- |
| [Ajax action pipeline]({{ '/scry-search-ajax/javascript/ajax-action-pipeline/' | relative_url }}) | Pre/post AJAX actions this add-on registers on each wrapped search form. |
| [Ajax JavaScript runtime]({{ '/scry-search-ajax/javascript/overview/' | relative_url }}) | Script: features/shortcode/assets/js/ajax.js Depends on: base plugin handle scry_ms_window-script (and optionally scry-search-facets) Localized object: scrySearchAjax (filterable via scry_ms_aj_ajax_localized) |
| [Base runtime]({{ '/scry-search-ajax/javascript/base-runtime/' | relative_url }}) | Pieces of window.scrySearch that this add-on uses. |
| [Extending from custom JS]({{ '/scry-search-ajax/javascript/extending-from-custom-js/' | relative_url }}) | Hook your own post-AJAX actions after the Ajax upgrade has registered. |
| [scrySearchAjax]({{ '/scry-search-ajax/javascript/scrysearchajax/' | relative_url }}) | Localized object for the Ajax shortcode script (filterable via scry_ms_aj_ajax_localized). |
| [ScrySearchAjax_SearchForm]({{ '/scry-search-ajax/javascript/scrysearchajax-searchform/' | relative_url }}) | Per-form controller for pagination, federation hidden inputs, and results rendering. |
| [Upgrade registration]({{ '/scry-search-ajax/javascript/registration/' | relative_url }}) | How the ajax upgrade registers on scrySearchReady and wraps matching forms. |

