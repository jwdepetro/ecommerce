# Generated by Django 2.1.2 on 2019-01-03 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_auto_20190103_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL),
        ),
    ]
