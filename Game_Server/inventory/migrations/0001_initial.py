# Generated by Django 2.0.2 on 2018-04-19 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('description', models.CharField(default='description', max_length=50)),
            ],
        ),
    ]
