# Generated by Django 3.2.3 on 2022-02-06 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220206_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='describe',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='describe',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
