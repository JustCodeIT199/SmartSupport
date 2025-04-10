# Generated by Django 5.1.7 on 2025-03-26 19:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_user_userprofile_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TASK_TITLE', models.CharField(max_length=100)),
                ('TASK_CREATED_ON', models.DateField(auto_now_add=True, null=True)),
                ('TASK_CLOSED_ON', models.DateField(null=True)),
                ('TASK_DUE_DATE', models.DateField()),
                ('TASK_ASSIGNED_TO', models.IntegerField()),
                ('TASK_DESCRIPTION', models.CharField(max_length=300)),
                ('TASK_STATUS', models.CharField(default='Open', max_length=100)),
                ('TASK_CLOSED', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CLOSED_BY', to=settings.AUTH_USER_MODEL)),
                ('TASK_CREATED', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CREATED_BY', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
