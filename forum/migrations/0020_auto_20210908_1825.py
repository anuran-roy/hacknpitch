# Generated by Django 3.2.7 on 2021-09-08 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0019_auto_20210908_1822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-votes', '-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['-votes', '-date']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='dislikes',
            new_name='votes',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='dislikes',
            new_name='votes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='likes',
        ),
    ]