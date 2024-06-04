# Generated by Django 4.2.6 on 2024-06-01 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0006_team_team_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='score',
        ),
        migrations.AddField(
            model_name='score',
            name='team_number',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='scoreboard.team'),
        ),
    ]
