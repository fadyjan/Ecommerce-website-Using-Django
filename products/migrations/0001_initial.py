# Generated by Django 3.0.3 on 2020-03-06 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
                ('product_details', models.CharField(max_length=500)),
                ('product_model', models.CharField(max_length=200)),
                ('product_average_rating', models.IntegerField(default=0)),
                ('product_count', models.IntegerField(default=0)),
            ],
        ),
    ]