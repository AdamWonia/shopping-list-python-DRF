# Generated by Django 3.0.14 on 2021-11-01 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=120)),
                ('amount', models.DecimalField(decimal_places=0, max_digits=2)),
                ('bought', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]