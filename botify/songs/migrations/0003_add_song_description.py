# Generated by Django 5.0.2 on 2024-04-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_change_name_artist_to_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
