# Generated by Django 3.2.5 on 2021-07-19 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='workouts',
            options={'verbose_name_plural': 'Workouts'},
        ),
    ]