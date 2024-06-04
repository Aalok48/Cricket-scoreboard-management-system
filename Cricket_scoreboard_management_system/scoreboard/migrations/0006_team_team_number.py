# Generated by Django 4.2.6 on 2024-06-01 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0005_alter_match_match_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_number',
            field=models.IntegerField(choices=[(1, 'Team 1'), (2, 'Team 2')], default=1),
        ),
    ]