# Generated by Django 3.2.9 on 2021-12-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mood_bot", "0005_tguser_crontab"),
    ]

    operations = [
        migrations.AddField(
            model_name="mood",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
