# Generated by Django 4.1 on 2022-09-13 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15, unique=True, verbose_name='NameProduct')),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
