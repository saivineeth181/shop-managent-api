# Generated by Django 3.2.3 on 2022-02-08 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_sale_sold_or_buy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='sold_or_buy',
            field=models.CharField(choices=[('sold', 'sold'), ('buy', 'buy')], max_length=50),
        ),
    ]