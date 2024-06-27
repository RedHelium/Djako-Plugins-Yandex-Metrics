from django.db import models


class YandexMetrikaCounter(models.Model):

    header = models.CharField(
        verbose_name="Заголовок", max_length=64, blank=False, null=False
    )
    counter = models.CharField(
        verbose_name="Код счётчика", max_length=16, blank=False, null=False
    )

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "Счётчик Яндекс метрики"
        verbose_name_plural = "Счётчики Яндекс метрики"


class YandexMetrikaWidgetStyle(models.Model):

    header = models.CharField(verbose_name="Заголовок", max_length=64)
    border_width = models.IntegerField(verbose_name="Толщина границы", default=1)
    fill = models.CharField(verbose_name="Тип заливки", max_length=10)
    line_tension = models.FloatField(verbose_name="Сглаживание линий", default=0.2)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "Стиль счётчика Яндекс метрики"
        verbose_name_plural = "Стили счётчика Яндекс метрики"


class YandexMetrikaCounterWidget(models.Model):

    header = models.CharField(verbose_name="Заголовок", max_length=150)
    display_label = models.CharField(
        verbose_name="Отображаемое имя диаграммы",
        max_length=150,
        null=True,
        blank=True,
    )

    counter = models.ForeignKey(
        YandexMetrikaCounter, verbose_name="Счётчик", on_delete=models.CASCADE
    )

    dateFrom = models.CharField(
        verbose_name="Период получения данных. От какого числа.",
        max_length=16,
        blank=True,
        null=True,
        help_text="Прописывается в формате YYYY-MM-DD",
    )
    dateTo = models.CharField(
        verbose_name="Период получения данных. До какого числа включительно.",
        max_length=16,
        blank=True,
        null=True,
        help_text="Прописывается в формате YYYY-MM-DD",
    )
    metrics = models.CharField(
        verbose_name="Метрики",
        max_length=250,
        help_text="Можно указать до 20 метрик в запросе. Синтаксис описан в документации Яндекс",
    )
    dimensions = models.CharField(
        verbose_name="Группировки",
        max_length=150,
        help_text="Можно указать до 10 группировок в запросе. Синтаксис описан в документации Яндекс",
    )
    limit = models.IntegerField(
        verbose_name="Макс. лимит на кол-во возвращаемых строк", default=100
    )
    style = models.ForeignKey(
        YandexMetrikaWidgetStyle,
        verbose_name="Стиль диаграммы",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    ordering = models.IntegerField(verbose_name="Приоритет отображения", default=0)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "Диаграмма счётчика"
        verbose_name_plural = "Диаграммы счётчика"
        ordering = ["-ordering"]
