# Generated by Django 5.0.3 on 2024-04-07 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adminstrator', '0028_alter_tbl_reply_reply_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_reply',
        ),
    ]