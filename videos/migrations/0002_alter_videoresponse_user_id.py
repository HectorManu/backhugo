# Generated by Django 5.0.2 on 2024-02-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoresponse',
            name='user_id',
            field=models.BigIntegerField(),
        ),
    ]
