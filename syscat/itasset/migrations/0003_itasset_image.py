# Generated by Django 3.2.14 on 2022-07-21 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itasset', '0002_auto_20220720_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='itasset',
            name='image',
            field=models.ImageField(blank=True, upload_to='itasset/', verbose_name='Картинка'),
        ),
    ]
