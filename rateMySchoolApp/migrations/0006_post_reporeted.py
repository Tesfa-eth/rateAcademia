# Generated by Django 4.0.3 on 2022-04-18 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rateMySchoolApp', '0005_post_edited'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reporeted',
            field=models.BooleanField(default=False),
        ),
    ]