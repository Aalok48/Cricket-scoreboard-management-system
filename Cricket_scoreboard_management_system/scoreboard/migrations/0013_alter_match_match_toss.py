# Generated by Django 4.2.6 on 2024-06-07 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0012_alter_match_match_toss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_toss',
            field=models.CharField(choices=[('Head', 'Head'), ('Tail', 'Tail')], max_length=4, null=True),
        ),
    ]
