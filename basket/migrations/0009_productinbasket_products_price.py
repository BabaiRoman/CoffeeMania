# Generated by Django 4.1.4 on 2023-06-13 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0008_alter_productinbasket_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='products_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
