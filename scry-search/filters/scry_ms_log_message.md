---
layout: doc
title: "scry_ms_log_message"
summary: "Modify a log message before it is stored."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Logs"
---

Modify a log message before it is stored.


|               |                                    |
| ------------- | ---------------------------------- |
| **Type**      | Filter                             |
| **Arguments** | `string $message`, `string $level` |
| **Returns**   | `string` — the message to store    |
| **When**      | Before each log entry is written.  |


`$level` is one of `debug` or `error`. Return the message string (modified or unchanged).
