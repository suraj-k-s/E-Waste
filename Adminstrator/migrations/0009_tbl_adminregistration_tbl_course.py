# Generated by Django 5.0.3 on 2024-03-12 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminstrator', '0008_delete_tbl_admin_delete_tbl_adminregistration_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_adminregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AdminRegistration_name', models.CharField(max_length=50)),
                ('AdminRegistration_contact', models.CharField(max_length=50)),
                ('AdminRegistration_email', models.CharField(max_length=50)),
                ('AdminRegistration_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=50)),
                ('Course_Duration', models.CharField(max_length=50)),
                ('Course_Fees', models.CharField(max_length=50)),
            ],
        ),
    ]