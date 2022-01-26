# Generated by Django 4.0.1 on 2022-01-26 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]
