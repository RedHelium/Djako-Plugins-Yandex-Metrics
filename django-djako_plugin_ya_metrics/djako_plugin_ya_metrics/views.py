import os
from django.http import JsonResponse
import requests

from .models import (
    YandexMetrikaCounter,
    YandexMetrikaCounterWidget,
    YandexMetrikaWidgetStyle,
)


def get_yandex_counter(request):

    API_URL = "https://api-metrika.yandex.ru/stat/v1/data"

    counters = YandexMetrikaCounter.objects.all()

    responseCtx = {"counter": ""}

    countersList = []

    for counter in counters:

        widgets = YandexMetrikaCounterWidget.objects.filter(
            counter=counter, hidden=False
        )

        headers = {
            "Authorization": "Bearer %s" % (os.environ.get("YANDEX_ACCESS_TOKEN"))
        }

        widgetsCtxList = []

        for widget in widgets:

            params = {
                "date1": widget.dateFrom,
                "date2": widget.dateTo,
                "id": counter.counter,
                "metrics": widget.metrics,
                "dimensions": widget.dimensions,
                "limit": widget.limit,
            }

            if widget.style is not None:
                counter_style = YandexMetrikaWidgetStyle.objects.get(id=widget.style.id)
            else:
                continue  # TODO Добавить загрузку дефолтного стиля

            try:
                response = requests.get(url=API_URL, headers=headers, params=params)
            except Exception as ex:
                return JsonResponse({"error": "Ошибка выполнения запроса! %s" % (ex)})

            data = response.json()

            datasets = []
            dimensions = []

            try:

                for row in data["data"]:
                    for dimension in row["dimensions"]:
                        dimensions.append(dimension["name"])
            except:
                return JsonResponse(
                    {
                        "error": "Ошибка в параметрах диаграммы '%s'! %s"
                        % (widget.header, data["message"])
                    }
                )

            totals = data["totals"]

            for index_dataset in range(len(totals)):

                metrics = []
                for row in data["data"]:
                    for index, metric in enumerate(row["metrics"]):
                        if index == index_dataset:
                            metrics.append(metric)

                splitLabel = widget.display_label.split(",")
                if len(splitLabel) > 1:
                    label = widget.display_label.split(",")[index_dataset]
                else:
                    label = widget.display_label

                ctx = {
                    "header": label,
                    "borderWidth": counter_style.border_width,
                    "fill": counter_style.fill,
                    "lineTension": counter_style.line_tension,
                    "values": metrics,
                }

                datasets.append({"dataset": ctx})

            widgetsCtxList.append(
                {
                    "id_chart": "chart-counter-%s-%s" % (counter.counter, widget.id),
                    "datasets": datasets,
                    "labels": dimensions,
                    "title": "%s - %s" % (widget.display_label, int(sum(totals))),
                    "chart_type": widget.style.chart_type,
                }
            )

        countersList.append(
            {"counter": {"number": counter.counter, "widgets": widgetsCtxList}}
        )

    responseCtx = {"counters": countersList}

    return JsonResponse(responseCtx)
