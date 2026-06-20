from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена (₽)")
    image_url = models.URLField(blank=True, null=True, verbose_name="Ссылка на картинку")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name