# Generated by Django 4.0.2 on 2022-02-16 04:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_products_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
