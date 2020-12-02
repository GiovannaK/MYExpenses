from django.db import models
from profiles.models import Profile
from expenses.models import Currencies


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome da categoria", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Earns(models.Model):
    currency = models.ForeignKey(Currencies, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Categoria")
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.CharField(max_length=800, verbose_name="Descrição")
    quantity = models.DecimalField(max_digits=19, decimal_places=2, verbose_name="Valor")
    date = models.DateField(verbose_name="Data")
    long_term = models.BooleanField(default=False, verbose_name="Ganho fixo")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-long_term'] 
        verbose_name = 'Ganho'
        verbose_name_plural = 'Ganhos'   

