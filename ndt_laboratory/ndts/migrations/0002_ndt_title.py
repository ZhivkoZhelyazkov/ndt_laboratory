# Generated by Django 3.1.4 on 2020-12-19 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ndts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ndt',
            name='title',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
