from django.db import models

# Create your models here.

class Match(models.Model):
    match_number = models.PositiveSmallIntegerField(unique = True, default=1, blank = False, null = False)
    match_date = models.DateField(auto_now_add = True, blank = False, null = False)
    match_location = models.CharField(max_length = 15, blank = False, null = False)

class Team(models.Model):
    match_number = models.ForeignKey(Match, on_delete = models.CASCADE, blank = False, null = False, default = 1)
    team_name = models.CharField(max_length =20, blank = False, null = False)
    team_coach = models.CharField(max_length = 10, blank = False, null = False)
    team_homeground = models.CharField(max_length = 15, blank = True, null = True)

class Player(models.Model):
    role = [
        ('BT', 'Batsman'),
        ('B', 'Bowler'),
        ('AR', 'All Rounder'),
    ]
    player_name = models.CharField(max_length=15, blank = False, null = False)
    player_age = models.PositiveSmallIntegerField(blank = False)
    player_team = models.ForeignKey(Team, on_delete = models.CASCADE, blank = False, null = False)
    match_number = models.ForeignKey(Match, on_delete = models.CASCADE, blank = False, null = False, default = 1)
    player_role = models.CharField(max_length = 2, choices = role)


class Score(models.Model):
    player = models.ForeignKey(Player, on_delete = models.CASCADE)
    match_number = models.ForeignKey(Match, on_delete = models.CASCADE, blank = False, null = False, default = 1)
    score = models.PositiveIntegerField()
    run = models.PositiveIntegerField()
    wickets = models.PositiveIntegerField()
    overs = models.PositiveIntegerField()