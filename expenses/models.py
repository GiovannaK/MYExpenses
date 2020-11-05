from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome da categoria")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
           

class Expenses(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Categoria", blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.CharField(max_length=800, verbose_name="Descrição")
    quantity = models.DecimalField(max_digits=19, decimal_places=2, verbose_name="Quantidade")
    date = models.DateField(verbose_name="Data")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'


