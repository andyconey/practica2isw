# Generated by Django 4.2.5 on 2023-10-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relecloud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='slug',
            field=models.SlugField(default='none'),
            preserve_default=False,
        ),
    ]