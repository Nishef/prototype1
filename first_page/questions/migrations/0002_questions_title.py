# Generated by Django 3.1 on 2020-08-17 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
