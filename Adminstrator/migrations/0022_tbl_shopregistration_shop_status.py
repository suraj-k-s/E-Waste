# Generated by Django 5.0.3 on 2024-03-15 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminstrator', '0021_tbl_shopregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_shopregistration',
            name='shop_status',
            field=models.IntegerField(default=0),
        ),
    ]