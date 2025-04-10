# Generated by Django 5.1.7 on 2025-03-27 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_taskdetail_task_holder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdetail',
            name='TASK_STATUS',
            field=models.CharField(choices=[('Open', 'Open'), ('Inprocess', 'Inprocess'), ('Closed', 'Closed'), ('Reopen', 'Reopen'), ('Expired', 'Expired'), ('Resolved', 'Resolved')], default='Open', max_length=100),
        ),
    ]
