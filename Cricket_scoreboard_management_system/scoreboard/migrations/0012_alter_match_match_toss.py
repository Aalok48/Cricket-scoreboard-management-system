# Generated by Django 4.2.6 on 2024-06-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0011_match_match_toss_score_extra_runs_score_no_four_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_toss',
            field=models.IntegerField(choices=[('Head', 'Head'), ('Tail', 'Tail')], null=True),
        ),
    ]
