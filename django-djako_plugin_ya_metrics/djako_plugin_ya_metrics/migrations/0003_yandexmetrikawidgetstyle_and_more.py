# Generated by Django 5.0.6 on 2024-06-26 22:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djako_plugin_ya_metrics', '0002_remove_yandexmetrikacounter_datefrom_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='YandexMetrikaWidgetStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=64, verbose_name='Заголовок')),
                ('border_width', models.IntegerField(default=1, verbose_name='Толщина границы')),
                ('fill', models.CharField(max_length=10, verbose_name='Тип заливки')),
                ('line_tension', models.FloatField(default=0.2, verbose_name='Сглаживание линий')),
            ],
            options={
                'verbose_name': 'Стиль счётчика Яндекс метрики',
                'verbose_name_plural': 'Стили счётчика Яндекс метрики',
            },
        ),
        migrations.AddField(
            model_name='yandexmetrikacounterwidget',
            name='display_label',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Отображаемое имя диаграммы'),
        ),
        migrations.AddField(
            model_name='yandexmetrikacounterwidget',
            name='style',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djako_plugin_ya_metrics.yandexmetrikawidgetstyle', verbose_name='Стиль диаграммы'),
        ),
    ]
