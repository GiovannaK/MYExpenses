# Generated by Django 3.1.3 on 2020-11-06 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0009_auto_20201106_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='currency',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='expenses.currencies'),
        ),
        migrations.AlterField(
            model_name='currencies',
            name='currency',
            field=models.CharField(default=None, max_length=255, verbose_name='Moeda'),
        ),
    ]
