# Photo & Video

Рабочая база знаний по фото-, видео- и кинооборудованию, кодекам и съёмочному workflow.

## Технические памятки

- [Sony α7S III / α6700 — видеосъёмка, S-Log3, ISO и экспозиция](sony.md)
- [Apple iPhone Pro 14–18 — камеры, Apple Log / Log 2, ProRes / RAW, PAL 25/50/100, bitrates и storage](apple-iphone-pro.md)

## Машиночитаемый каталог оборудования

**Точка входа для агентов:** [`catalog/index.yaml`](catalog/index.yaml).

- [Типы оборудования](catalog/types.yaml) и [JSON Schemas](catalog/schemas/).
- [Архитектура каталога](docs/catalog/architecture.md) — модели, экземпляры, характеристики, совместимость.
- [Зафиксированные требования и решения](docs/catalog/requirements-and-decisions.md).
- [Масса и конфигурации съёмки](docs/catalog/measurements-and-rigs.md).
- [Мультиязычность](docs/catalog/internationalization.md) — English primary, Russian supported.
- [Фотографии и права](docs/catalog/media-policy.md).
- [Будущий публичный сайт](docs/catalog/public-site.md).
- [План внедрения](docs/catalog/roadmap.md).
- [Инструкции AI-агентам](AGENTS.md).

Каталог хранит **характеристики модели** отдельно от **конкретного экземпляра в инвентаре**. Покупка не следует из простого обсуждения модели. `catalog/` развивается независимо от существующих статей; статьи служат техническими источниками и справочными материалами.

Документация на русском языке, идентификаторы, поля данных и базовая локаль каталога — на английском.
