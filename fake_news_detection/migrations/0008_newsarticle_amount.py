# Generated by Django 3.2 on 2022-10-26 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake_news_detection', '0007_auto_20221026_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='amount',
            field=models.IntegerField(default=10),
        ),
    ]
