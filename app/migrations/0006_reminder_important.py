# Generated by Django 5.1.1 on 2024-11-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_reminder_user_alter_reminder_reminder_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="reminder",
            name="important",
            field=models.BooleanField(default=False),
        ),
    ]