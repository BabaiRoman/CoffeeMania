# Generated by Django 4.1.4 on 2023-06-06 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
