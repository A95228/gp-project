# Generated by Django 3.0.2 on 2020-02-23 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_userscore'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userscore',
            name='exam_id',
        ),
        migrations.AddField(
            model_name='userscore',
            name='exam_title',
            field=models.CharField(default='default', max_length=300),
            preserve_default=False,
        ),
    ]
