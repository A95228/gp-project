# Generated by Django 3.0.2 on 2020-06-16 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20200528_0109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtopic',
            name='subtopic_status',
        ),
        migrations.AddField(
            model_name='subtopic',
            name='subtopic_detail',
            field=models.TextField(default='this sfids  fsa s fll aflaif ilsa flais lf asl flasf salininflanclksnmclams os fn sofo', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subtopic',
            name='subtopic_image_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_detail',
            field=models.TextField(default='dsfl s lk slfjljs fjlac  ac l ajl a ls df a f sa fl w e fw elr wer wer w erwer we r we r we rwe rwefdsfsdc sd  sd', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_status',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
