# Generated by Django 3.2.3 on 2022-02-08 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20220209_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sale',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.item'),
        ),
    ]