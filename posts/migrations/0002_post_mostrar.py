# Generated by Django 4.1.1 on 2022-09-26 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
    ]
