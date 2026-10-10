---
layout: doc
title: "Plugin lifecycle"
heading: "Plugin lifecycle"
summary: "What happens on deactivation and uninstall."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: guide
doc_type_label: "Guide"
type_url: "/scry-search/guides/"
category: "Basics"
---

- **Deactivation** — clears daily WP-Cron hooks (`scry_ms_cleanup_analytics_events`, `scry_ms_cleanup_logs`). Options, tables, and Meilisearch indexes are kept.
- **Uninstall** (`uninstall.php`) — drops `{prefix}scry_ms_search_analytics` and `{prefix}scry_ms_logs`, deletes all `scry_ms_*` options (including connection keys and index settings backups), and clears cron again. Does **not** delete remote Meilisearch indexes.

Implementation: `includes/class-lifecycle.php`, registered from `scry_search.php` / `uninstall.php`.

---
