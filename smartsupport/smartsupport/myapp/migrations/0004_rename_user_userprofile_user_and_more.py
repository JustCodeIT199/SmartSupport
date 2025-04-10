# Generated by Django 5.1.7 on 2025-03-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_userprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='User',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='RegistratioNo',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='RegistrationNo',
            field=models.CharField(default='0000CE00F', max_length=100),
        ),
    ]
