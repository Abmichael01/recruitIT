# Generated by Django 4.2.10 on 2024-04-03 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0005_application_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='recruitment',
            options={'ordering': ['-created']},
        ),
    ]
