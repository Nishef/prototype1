# Generated by Django 3.1 on 2020-08-18 10:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_questions_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questions',
            options={'ordering': ['-created_at', '-updated_at']},
        ),
        migrations.AddField(
            model_name='questions',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='title',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]