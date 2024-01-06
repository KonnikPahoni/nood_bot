# Generated by Django 3.2.9 on 2021-12-05 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("django_celery_beat", "0015_edit_solarschedule_events_choices"),
        ("mood_bot", "0002_alter_mood_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="tguser",
            name="task",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="django_celery_beat.periodictask",
            ),
        ),
        migrations.AlterField(
            model_name="mood",
            name="value",
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
