# Generated by Django 4.2.5 on 2023-10-18 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relecloud', '0005_inforequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50)),
                ('comment', models.TextField(max_length=2000)),
            ],
        ),
    ]