# Generated by Django 3.2.6 on 2021-09-12 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='image', verbose_name='عكس'),
        ),
    ]
