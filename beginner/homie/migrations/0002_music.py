# Generated by Django 5.1.2 on 2024-10-29 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_name', models.TextField(max_length=200)),
                ('music_description', models.TextField(max_length=200)),
            ],
        ),
    ]