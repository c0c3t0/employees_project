# Generated by Django 4.0.2 on 2022-02-04 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees_app', '0003_alter_employee_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='egn',
            field=models.CharField(default='', max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, max_length=49, null=True),
        ),
    ]
