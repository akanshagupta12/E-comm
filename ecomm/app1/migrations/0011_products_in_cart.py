# Generated by Django 4.0.2 on 2022-02-24 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_razorpay_razorpay_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='in_cart',
            field=models.BooleanField(default=False),
        ),
    ]