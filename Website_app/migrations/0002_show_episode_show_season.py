# Generated by Django 4.2.7 on 2023-11-03 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='episode',
            field=models.CharField(default=None, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='show',
            name='season',
            field=models.CharField(default=None, max_length=3),
            preserve_default=False,
        ),
    ]
