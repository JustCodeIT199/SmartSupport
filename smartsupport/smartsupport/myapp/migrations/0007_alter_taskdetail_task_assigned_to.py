# Generated by Django 5.1.7 on 2025-03-27 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_taskdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdetail',
            name='TASK_ASSIGNED_TO',
            field=models.IntegerField(null=True),
        ),
    ]
