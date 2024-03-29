# Generated by Django 4.2.5 on 2023-10-02 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relecloud', '0002_destination_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cruise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=2000)),
                ('destinations', models.ManyToManyField(related_name='destinations', to='relecloud.destination')),
            ],
        ),
    ]
