# Generated by Django 4.0.2 on 2022-02-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_products_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mrp', models.IntegerField()),
                ('csp', models.IntegerField(default=0.0)),
                ('image', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
