# Generated by Django 2.1.2 on 2019-01-04 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='last_used_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='primary',
            field=models.BooleanField(default=False),
        ),
    ]
