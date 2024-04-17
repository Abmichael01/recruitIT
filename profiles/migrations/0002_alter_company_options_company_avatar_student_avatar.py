# Generated by Django 4.2.10 on 2024-03-17 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Companie'},
        ),
        migrations.AddField(
            model_name='company',
            name='avatar',
            field=models.ImageField(default='avatar.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='student',
            name='avatar',
            field=models.ImageField(default='avatar.png', null=True, upload_to=''),
        ),
    ]
