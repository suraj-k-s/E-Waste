# Generated by Django 5.0.3 on 2024-03-22 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminstrator', '0023_delete_tbl_shopregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_ewaste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ewaste_name', models.CharField(max_length=50)),
                ('ewaste_details', models.CharField(max_length=50)),
                ('ewaste_price', models.CharField(max_length=50)),
                ('ewaste_image', models.FileField(upload_to='Assets/ewasteimage/')),
            ],
        ),
    ]