# Generated by Django 3.0.5 on 2020-05-16 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_movies_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='poster',
        ),
    ]
