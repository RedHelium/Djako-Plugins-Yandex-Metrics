from django.contrib import admin

from .models import (
    YandexMetrikaCounter,
    YandexMetrikaCounterWidget,
    YandexMetrikaWidgetStyle,
)


@admin.register(YandexMetrikaCounter)
class YandexMetrikaCounterAdmin(admin.ModelAdmin):
    list_display = ("header", "id")


@admin.register(YandexMetrikaCounterWidget)
class YandexMetrikaCounterWidgetAdmin(admin.ModelAdmin):
    list_display = ("header", "counter", "dateFrom", "dateTo", "dimensions", "metrics")
    list_editable = ("dateFrom", "dateTo", "dimensions", "metrics")
    change_list_template = 'admin/djako_yandex_metrics/widgets.html'


@admin.register(YandexMetrikaWidgetStyle)
class YandexMetrikaWidgetStyleAdmin(admin.ModelAdmin):
    list_display = ("header",)
