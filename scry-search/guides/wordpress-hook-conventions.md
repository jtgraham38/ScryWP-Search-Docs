---
layout: doc
title: "WordPress hook conventions"
heading: "WordPress hook conventions"
summary: "Filters return values; actions are for side effects."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: guide
doc_type_label: "Guide"
type_url: "/scry-search/guides/"
category: "Basics"
---

A quick reminder of the WordPress conventions used throughout:

- **Filters** receive a value and **must return a value** (modified or not).
- **Actions** return nothing; they are for side effects.
- If your callback wants more than the first argument, declare the argument count in the 4th parameter of `add_filter()` / `add_action()`.

---
