# Generated by Django 3.1.3 on 2020-11-05 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20201105_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default='Escreva sobre você...', max_length=300, null=True, verbose_name='Conte-nos sobre você'),
        ),
    ]