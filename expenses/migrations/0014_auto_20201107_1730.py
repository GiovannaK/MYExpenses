# Generated by Django 3.1.3 on 2020-11-07 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0013_auto_20201107_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='expenses.category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='currency',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='expenses.currencies'),
        ),
    ]
