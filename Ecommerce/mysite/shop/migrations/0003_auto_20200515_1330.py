# Generated by Django 2.2.6 on 2020-05-15 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='item_id',
            new_name='items',
        ),
    ]
