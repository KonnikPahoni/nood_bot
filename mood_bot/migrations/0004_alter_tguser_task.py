# Generated by Django 3.2.9 on 2021-12-05 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("django_celery_beat", "0015_edit_solarschedule_events_choices"),
        ("mood_bot", "0003_auto_20211205_1608"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tguser",
            name="task",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="user",
                to="django_celery_beat.periodictask",
            ),
        ),
    ]
