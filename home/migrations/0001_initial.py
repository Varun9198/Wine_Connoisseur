# Generated by Django 2.1.7 on 2019-02-17 04:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('COUNTRY', models.CharField(max_length=20)),
                ('DESCRIPTION', models.CharField(max_length=50)),
                ('DESIGNATION', models.CharField(max_length=20)),
                ('POINTS', models.IntegerField(default=0)),
                ('PRICE', models.IntegerField(default=0)),
                ('PROVINCE', models.CharField(max_length=20)),
                ('REGION_1', models.CharField(max_length=20)),
                ('REGION_2', models.CharField(max_length=20)),
                ('VARIETY', models.CharField(max_length=20)),
                ('WINERY', models.CharField(max_length=40)),
            ],
        ),
    ]
