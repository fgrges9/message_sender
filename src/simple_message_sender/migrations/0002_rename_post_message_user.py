# Generated by Django 4.2.4 on 2023-08-14 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_message_sender', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='post',
            new_name='user',
        ),
    ]
