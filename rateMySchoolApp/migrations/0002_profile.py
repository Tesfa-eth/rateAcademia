# Generated by Django 4.0.3 on 2022-04-03 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rateMySchoolApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default=sqlalchemy.sql.expression.null, max_length=20)),
                ('lastName', models.CharField(default=sqlalchemy.sql.expression.null, max_length=20)),
                ('bio', models.TextField()),
                ('verified', models.BooleanField(default=False)),
                ('blocked', models.BooleanField(default=False)),
                ('reported', models.IntegerField(default=0)),
                ('bagdeValue', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
