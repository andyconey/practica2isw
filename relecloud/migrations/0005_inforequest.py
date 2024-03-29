# Generated by Django 4.2.5 on 2023-10-08 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relecloud', '0004_alter_cruise_destinations'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('notes', models.TextField(max_length=2000)),
                ('cruise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='relecloud.cruise')),
            ],
        ),
    ]
