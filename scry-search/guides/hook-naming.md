---
layout: doc
title: "Hook naming"
heading: "Hook naming"
summary: "Every PHP hook is namespaced with the scry_ms_ prefix."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: guide
doc_type_label: "Guide"
type_url: "/scry-search/guides/"
category: "Basics"
---

Every PHP hook in this plugin is namespaced with the prefix:

```
scry_ms_
```

So a hook documented below as `index_prepare_document` is registered in WordPress as `scry_ms_index_prepare_document`.

```php
add_filter( 'scry_ms_index_prepare_document', 'my_callback' );
```

> All hook names below are shown **with** their full, literal `scry_ms_` prefix so you can copy them directly.

---
