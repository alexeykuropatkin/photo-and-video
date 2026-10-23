# Internationalization (i18n) — English primary, Russian fully supported

## Decision

- Default locale `en`; support `ru` from day one. Future locales should require translations but **not** schema migrations.
- Data IDs, field keys, manufacturer names and enumerated values are language-neutral and never translated. Human-readable labels, help descriptions, alt text, marketing copy, comparison explanations and page SEO data are localizable.
- Base dictionaries are `catalog/locales/en.yaml` and `catalog/locales/ru.yaml`; localized per-model editorial content may live at `catalog/locales/models/<locale>/<model-id>.yaml`. This avoids inserting every new language into every specs record.
- Never use translated labels for database joins or URL IDs.
- Fallback `ru -> en` for missing *optional* editorial copy; **mandatory interface and spec labels must exist in both en and ru**, validated in CI.
- Support localized enum choices, pluralization, number/unit formatting, sorting/search aliases and transliteration. Model/product trademarks normally remain unchanged.
- Suggested site URL structure is `/en/equipment/<stable-id>` and `/ru/equipment/<stable-id>`. Language selection should persist in client UX with a predictable en default; use correct `lang`, `hreflang` and canonical metadata.
- Technical docs may remain in Russian; public product source data and data contracts are written in English.

## Examples

`lens.specs.filter.front_thread_mm = 82` is canonical; the interface displays “Filter thread: 82 mm” in en and “Резьба под фильтр: 82 мм” in ru. An enum `global` is stored unchanged, presented as “Global shutter” / “Глобальный затвор”.

Localization files are UI resources, **not alternate sources of technical facts**. Avoid localizing units by changing data (e.g., multiplying focal length by a crop factor). Use dedicated calculated display fields if comparisons require equivalent fields of view.
