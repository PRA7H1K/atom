# Generated by Django 3.1.2 on 2021-01-13 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort', '0002_auto_20210111_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='long_url',
            field=models.URLField(max_length=700, verbose_name=' '),
        ),
    ]