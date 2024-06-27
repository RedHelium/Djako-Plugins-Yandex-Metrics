from django.urls import re_path

from .views import get_yandex_counter

urlpatterns = [
    re_path(r"^api/v1/metrika/counter/$", get_yandex_counter),
]
