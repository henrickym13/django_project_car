# Generated by Django 4.2.5 on 2023-12-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0007_continente_slug_marca_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='url_video',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
