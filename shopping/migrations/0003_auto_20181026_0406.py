# Generated by Django 2.1.2 on 2018-10-26 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_cart_session_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='shopping.Cart'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='qty',
            field=models.IntegerField(default=0),
        ),
    ]
