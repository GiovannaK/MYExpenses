# Generated by Django 3.1.3 on 2020-11-06 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_remove_profile_created'),
        ('expenses', '0003_expenses_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='exp', to='profiles.profile'),
        ),
    ]
