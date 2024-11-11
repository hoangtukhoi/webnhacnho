# Generated by Django 5.1.1 on 2024-11-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_reminder_user_alter_reminder_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='user',
        ),
        migrations.AddField(
            model_name='reminder',
            name='repeat',
            field=models.CharField(choices=[('once', 'Once'), ('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], default='once', max_length=10),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='reminder',
            field=models.CharField(max_length=255),
        ),
    ]
