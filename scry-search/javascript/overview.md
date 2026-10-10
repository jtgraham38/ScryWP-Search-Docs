---
layout: doc
title: "JavaScript runtime overview"
heading: "JavaScript runtime overview"
summary: "The plugin ships a small front‑end runtime, window.scrySearch, that discovers search forms on the page and gives you ordered hooks to run code before/after a search — both for normal submits and AJAX submits (used by aut…"
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: javascript
doc_type_label: "JavaScript API"
type_url: "/scry-search/javascript/"
category: "Runtime"
---

The plugin ships a small front‑end runtime, `window.scrySearch`, that discovers search forms on the page and gives you ordered hooks to run code before/after a search — both for normal submits and AJAX submits (used by autosuggest and similar features).

The script is enqueued on the front end. Other scripts can declare it as a dependency using the handle `scry_ms_window-script`. Configuration is exposed as `windowLocalized` (not a shared `localized` global).
