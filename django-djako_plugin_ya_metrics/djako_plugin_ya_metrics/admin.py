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
    list_display = ("header", "counter", "display_label")
    change_list_template = 'admin/yandex_metrika/widgets.html'


@admin.register(YandexMetrikaWidgetStyle)
class YandexMetrikaWidgetStyleAdmin(admin.ModelAdmin):
    list_display = ("header",)
