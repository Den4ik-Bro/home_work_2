from django.db import models
from django.core.validators import MinValueValidator


class Table(models.Model):
    date = models.DateField(verbose_name='Дата')
    title = models.CharField(max_length=25, verbose_name='Название')
    count = models.PositiveIntegerField(verbose_name='Количество')
    distance = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name='Расстояние в км',
        validators=(MinValueValidator(1.00, message='Расстояние должно быть больше нуля!'),)
    )

    class Meta:
        verbose_name = 'Таблица'
        verbose_name_plural = 'Таблицы'
        ordering = ('title', 'count', 'distance')

    def __str__(self):
        return f'{self.title}'