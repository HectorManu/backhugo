# Generated by Django 5.0.2 on 2024-02-20 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('video_name', models.CharField(max_length=255)),
                ('response', models.TextField()),
            ],
        ),
    ]