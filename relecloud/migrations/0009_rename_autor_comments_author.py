# Generated by Django 4.2.5 on 2023-10-18 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relecloud', '0008_comments_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='autor',
            new_name='author',
        ),
    ]
