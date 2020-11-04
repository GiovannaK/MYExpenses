from django.db import models
from django.utils.text import slugify


class Expenses(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.CharField(max_length=800, verbose_name="Descrição")
    quantity = models.DecimalField(max_digits=19, decimal_places=2, verbose_name="Quantidade")
    date = models.DateField(verbose_name="Data")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome da categoria")
    slug = models.SlugField(unique=True, blank=True, null=True)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.name)}'
            self.slug = slug
