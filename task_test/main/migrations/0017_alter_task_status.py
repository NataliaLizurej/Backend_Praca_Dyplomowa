# Generated by Django 3.2.8 on 2021-12-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Created', 'Created'), ('In proccess', 'In proccess'), ('Done', 'Done'), ('Closed', 'Closed')], default='Created', max_length=25, null=True),
        ),
    ]
