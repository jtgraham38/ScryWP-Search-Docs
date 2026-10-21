---
layout: list
title: "Guides — Scry Search Ajax"
summary: "Concepts and setup notes for Scry Search Ajax."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: guide
doc_type_label: "Guide"
list_kind: type
show_filter_search: false
---

### Basics

| Name | Summary |
| ---- | ------- |
| [Ajax upgrade overview]({{ '/scry-search-ajax/guides/overview/' | relative_url }}) | Premium add-on hooks use scry_ms_aj_; shared main-plugin hooks keep the scry_ms_ prefix. |

### Integration

| Name | Summary |
| ---- | ------- |
| [Shared main-plugin hooks]({{ '/scry-search-ajax/guides/shared-main-plugin-hooks/' | relative_url }}) | These use the main plugin prefix scry_ms_. This plugin either applies them (so other code can filter shared behavior) or listens to them (integration with the main upgrades UI). |

