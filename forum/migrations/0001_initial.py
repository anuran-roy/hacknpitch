# Generated by Django 3.2.7 on 2021-09-05 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='(Not available)', max_length=100)),
                ('description', models.TextField(default='(Not available)', max_length=750)),
                ('image', models.ImageField(upload_to='forum/images')),
            ],
        ),
    ]