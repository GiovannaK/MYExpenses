# Generated by Django 3.1.3 on 2021-01-04 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0018_expenses_long_term'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expenses',
            options={'ordering': ['-long_term'], 'verbose_name': 'Gasto', 'verbose_name_plural': 'Gastos'},
        ),
    ]
