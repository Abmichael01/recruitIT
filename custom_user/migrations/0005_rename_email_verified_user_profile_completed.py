# Generated by Django 4.2.10 on 2024-04-19 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0004_user_verification_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_verified',
            new_name='profile_completed',
        ),
    ]
