from django.db import models
from profiles.models import Profile
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome da categoria", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
           

class Currencies(models.Model):
    currency = models.CharField(max_length=20, default=None, verbose_name="Moeda")

    def __str__(self):
        return self.currency

        class Meta:
            verbose_name = 'Moeda'
            verbose_name_plural = 'Moedas'                           


class Expenses(models.Model):
    currency = models.ForeignKey(Currencies, on_delete=models.CASCADE, verbose_name="Moeda")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, 
    related_name="exp", default=None)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, 
    verbose_name="Categoria")
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.CharField(max_length=800, verbose_name="Descrição")
    quantity = models.DecimalField(max_digits=19, decimal_places=2, 
    verbose_name="Valor")
    date = models.DateField(verbose_name="Data")
    long_term = models.BooleanField(default=False, verbose_name="Gasto fixo")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-long_term']
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'




                