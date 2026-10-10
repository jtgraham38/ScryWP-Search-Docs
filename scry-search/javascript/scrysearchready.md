---
layout: doc
title: "scrySearchReady"
summary: "Event dispatched on document after forms are discovered — wait for this before using the API."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: javascript
doc_type_label: "JavaScript API"
type_url: "/scry-search/javascript/"
category: "Runtime"
---

The runtime initializes on `DOMContentLoaded`, finds the search forms, and then dispatches a `scrySearchReady` event on `document`. **Always wait for this event** before touching the API, so you don't depend on script load order.

```js
document.addEventListener('scrySearchReady', function (e) {
    const { version, searchForms, upgrades } = e.detail;
    // searchForms is an array of ScrySearch_SearchForm instances
});
```
