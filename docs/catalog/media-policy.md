# Catalog product media and licensing

## Goals

Provide instant visual identification of models in GitHub, AI-supported answers, and an eventual web UI. Product images are not specifications, and assets must never silently imply an owned instance.

## Layout

```text
assets/
  cameras/<model-id>/hero.webp
  lenses/<model-id>/hero.webp
  mount-adapters/<model-id>/hero.webp
  gimbals/<model-id>/hero.webp
  batteries/<model-id>/hero.webp
  cages/<model-id>/hero.webp
```

A model's `media` array refers to a relative asset path **or** remote original URL, includes a view key (`hero`, `front`, `back`, `mount`, `side`, `ports`), rights holder, license/permission basis, source URL, captured/verified date and optional alt-text translation key. A relative file must exist; remote files should have a fallback.

## Licensing policy

Do not copy images directly from product pages, shopping previews, or search engines merely because they are publicly visible. Obtain redistribution permission (press kit/explicit license), use personally photographed product images, or retain only a source URL until licensing is resolved. A downloaded product image without confirmed rights must not be committed to this public repository.

Store small optimized WebP assets (~1000-1200 px on the long edge) for approved copies; avoid full-size RAW photos and high-resolution originals in Git. Keep image hashes or file integrity metadata for deterministic rebuilds. Exclude EXIF containing personal locations from public copies. Do not treat externally hosted images as permanent or hotlink them without permission.
