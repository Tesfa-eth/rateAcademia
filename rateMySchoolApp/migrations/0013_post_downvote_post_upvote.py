# Generated by Django 4.0.3 on 2022-04-22 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rateMySchoolApp', '0012_alter_post_postreportedusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='downvote',
            field=models.ManyToManyField(blank=True, null=True, related_name='downvote', to='rateMySchoolApp.profile'),
        ),
        migrations.AddField(
            model_name='post',
            name='upvote',
            field=models.ManyToManyField(blank=True, null=True, related_name='upvote', to='rateMySchoolApp.profile'),
        ),
    ]
