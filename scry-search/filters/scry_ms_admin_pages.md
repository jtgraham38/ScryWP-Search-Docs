---
layout: doc
title: "scry_ms_admin_pages"
summary: "Inject, remove, or reorder tabs in the Scry Search admin shell."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Admin UI"
---

Inject, remove, or reorder tabs in the Scry Search admin shell.


|               |                                                                   |
| ------------- | ----------------------------------------------------------------- |
| **Type**      | Filter                                                            |
| **Arguments** | `array $registered_pages` (map of slug => page data)              |
| **Returns**   | `array`                                                           |
| **When**      | Whenever registered admin pages are read for the tab UI / assets. |


Each page entry includes `slug`, `label`, `icon`, `description`, and `url`.
