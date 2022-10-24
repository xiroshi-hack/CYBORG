# Generated by Django 4.1.2 on 2022-10-24 09:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyborg', '0006_games_alter_library_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('name', models.CharField(default='game name', max_length=40)),
                ('type', models.CharField(default='sandbox', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='library',
            name='date',
            field=models.TimeField(default=datetime.datetime(2022, 10, 24, 9, 49, 56, 833505, tzinfo=datetime.timezone.utc)),
        ),
    ]