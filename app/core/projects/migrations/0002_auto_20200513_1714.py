# Generated by Django 2.2.12 on 2020-05-13 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='DescProy',
            field=models.TextField(null=True, verbose_name='Descipcion del proyecto'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='UrlRepo',
            field=models.TextField(null=True, verbose_name='Url del repositorio del proyecto'),
        ),
    ]
