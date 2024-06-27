# Djako Plugin Yandex Metrics


Плагин для Djako, который предоставляет 
интеграцию с API Яндекс метрики и визуализирует счётчики через Chart.js

## Быстрый старт
-----------

1. Добавьте "djako_plugin_ya_metrics" в INSTALLED_APPS::

    INSTALLED_APPS = [
        ...,
        "djako_plugin_ya_metrics",
    ]

2. Добавьте маршруты плагина в urls.py проекта::

    path("", include("djako_plugin_ya_metrics.urls")),

3. Запустите ``python manage.py migrate`` для создания моделей.

4. Перейдите в панель админа, затем добавьте сначала счётчик, стиль диаграмм, а затем сами диаграммы.