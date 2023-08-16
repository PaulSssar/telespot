from django.db import models
from .validators import validate_year


class Cities(models.Model):
    city = models.CharField(
        'Город',
        unique=True,
        max_length=30,
    )

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.city


class PlanProfit(models.Model):
    profit = models.IntegerField(
        'Сумма прибыли (план)',
    )
    city = models.ForeignKey(
        Cities,
        verbose_name='Город',
        related_name='plan_profit',
        on_delete=models.CASCADE
    )
    year = models.IntegerField(
        'Год',
        validators=[validate_year, ]
    )

    class Meta:
        unique_together = ('year', 'city')
        verbose_name = 'Прибыль(план)'
        verbose_name_plural = 'Прибыль(план)'

    def __str__(self):
        return f'Город: {self.city}, год: {self.year}'


class ActualProfit(models.Model):
    profit = models.IntegerField(
        'Сумма прибыли (факт)',
    )
    city = models.ForeignKey(
        Cities,
        verbose_name='Город',
        related_name='actual_profit',
        on_delete=models.CASCADE
    )
    year = models.IntegerField(
        'Год',
        validators=[validate_year, ]
    )

    class Meta:
        verbose_name = 'Прибыль(факт.)'
        verbose_name_plural = 'Прибыль(факт.)'
        unique_together = ('year', 'city')

    def __str__(self):
        return f'Город: {self.city}, год: {self.year}'
