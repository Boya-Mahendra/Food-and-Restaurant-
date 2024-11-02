# Generated by Django 5.1 on 2024-09-21 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('Fid', models.IntegerField(primary_key=True, serialize=False)),
                ('FoodName', models.CharField(max_length=50)),
                ('FoodPrice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Restorent',
            fields=[
                ('RId', models.IntegerField(primary_key=True, serialize=False)),
                ('RName', models.CharField(max_length=50)),
                ('RLocation', models.TextField(max_length=120)),
            ],
        ),
    ]