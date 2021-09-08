# Generated by Django 3.2.7 on 2021-09-08 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0018_remove_comment_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-likes', 'dislikes', '-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['-likes', 'dislikes', '-date']},
        ),
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='issue',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='issue',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]