# Generated by Django 5.0.3 on 2024-03-18 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0005_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_newuser',
        ),
    ]