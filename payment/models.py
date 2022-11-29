from django.db import models


class Item(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наименование товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.FloatField(verbose_name='Цена')  # копейки

    def __str__(self):
        return self.name

    def get_display_price(self):
        return f'{self.price/100}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
