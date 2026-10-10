---
layout: doc
title: "window.scrySearch"
summary: "Global runtime object: version, form getters, and registerUpgrade()."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: javascript
doc_type_label: "JavaScript API"
type_url: "/scry-search/javascript/"
category: "Runtime"
---

| Member                             | Type                                  | Description                                                       |
| ---------------------------------- | ------------------------------------- | ----------------------------------------------------------------- |
| `version`                          | `string`                              | Runtime version.                                                  |
| `getSearchForms()`                 | `() => ScrySearch_SearchForm[]`       | All detected search forms.                                        |
| `getSearchFormsByClass(className)` | `(string) => ScrySearch_SearchForm[]` | Search forms whose `<form>` has the given CSS class.              |
| `registerUpgrade(name, version)`   | `(string, string) => void`            | Register a named extension namespace (see [Upgrades]({{ '/scry-search/javascript/upgrades/' | relative_url }})). |


A “search form” is any `<form>` matched by `windowLocalized.searchFormSelectors` (see [Form discovery]({{ '/scry-search/javascript/form-discovery/' | relative_url }})).
