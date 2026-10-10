---
layout: doc
title: "Upgrades"
heading: "Upgrades"
summary: "Reserve a namespace on window.scrySearch.upgrades for premium add-ons."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: javascript
doc_type_label: "JavaScript API"
type_url: "/scry-search/javascript/"
category: "Runtime"
---

`registerUpgrade(name, version)` reserves a namespace on `window.scrySearch.upgrades[name]` (a `ScrySearch_Upgrade` with `name`, `version`, and a `data` object) for larger add‑ons to store their own state. Registering the same name twice is ignored.

```js
window.scrySearch.registerUpgrade('my_addon', '1.0.0');
window.scrySearch.upgrades.my_addon.data.enabled = true;
```
