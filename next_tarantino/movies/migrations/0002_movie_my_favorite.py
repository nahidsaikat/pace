# Generated by Django 4.0.5 on 2022-07-02 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='my_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
