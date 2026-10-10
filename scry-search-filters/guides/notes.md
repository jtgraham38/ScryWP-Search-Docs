---
layout: doc
title: "Notes & unsupported surfaces"
heading: "Notes & unsupported surfaces"
summary: "These are hooks fired by this add-on. The plugin also consumes base Scry Search hooks prefixed scry_ms_ (see README.md) — e.g. scry_ms_multi_search_query, scry_ms_analytics_event_to_insert, scry_ms_premium_upgrade_settin…"
plugin: scry-search-filters
plugin_name: "Scry Search Filters"
plugin_url: "/scry-search-filters/"
doc_type: guide
doc_type_label: "Guide"
type_url: "/scry-search-filters/guides/"
category: "Guides"
---

- These are hooks fired *by* this add-on. The plugin also *consumes* base Scry Search hooks prefixed `scry_ms_` (see `[README.md](README.md)`) — e.g. `scry_ms_multi_search_query`, `scry_ms_analytics_event_to_insert`, `scry_ms_premium_upgrade_settings_ui`, `scry_ms_premium_upgrades_display`.
- The Gutenberg **Search Facets** block and related index-admin hooks are not currently registered in `[scry_search_facets.php](scry_search_facets.php)`; the shortcode + search + analytics path is the supported surface.
- Code that still exists but is not wired (e.g. federation facet helpers, index-document filters) should not be treated as public API until re-enabled.
- Dependency guard and premium-upgrade settings chrome (beyond the shortcode generator) are not public customization surfaces.
