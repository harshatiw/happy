# Generated by Django 3.0.6 on 2020-05-21 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='img',
        ),
        migrations.AddField(
            model_name='order',
            name='offer',
            field=models.BooleanField(default=False),
        ),
    ]
