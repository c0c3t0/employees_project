# Generated by Django 4.0.2 on 2022-02-04 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees_app', '0002_employee_first_name_employee_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=49, null=True),
        ),
    ]
