# Generated by Django 3.2.6 on 2021-09-23 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_order_transaction_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'مورد', 'verbose_name_plural': 'موارد'},
        ),
    ]
