from django.shortcuts import render, HttpResponse, redirect
from .models import Match, Team, Player, Score
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def newsandupdates(request):
    return HttpResponse("News and updates page")
    
def about(request):
    return HttpResponse("About page called")
    
def contact(request):
    return HttpResponse("Contact page called")
    
def help(request):
    return HttpResponse("Help page called")
    

from .models import Match

def add_match(request):
    if request.method == "POST":
        match_number = request.POST.get('match_number')
        match_location = request.POST.get('match_location')
        match_over = request.POST.get('match_over')

        match = Match(
            match_number=match_number,
            match_location=match_location,
            match_over=match_over
        )
        match.save()

        team1_select = request.POST.get('team1_select')
        team1_name = request.POST.get('team1_name')
        team1_coach = request.POST.get('team1_coach')
        team1_homeground = request.POST.get('team1_homeground')
        team1_select = 1 if team1_select == 'Team 1' else 2

        team1 = Team(
            team_name = team1_name,
            team_coach = team1_coach,
            team_homeground = team1_homeground,
            match_number = match,
            team_number = team1_select
        )
        team1.save()

        for i in range(1, 4):
            player_name = request.POST.get(f'player{i}_team1')
            player_role = request.POST.get(f'team1_player{i}_role')
            if player_name:
                player = Player(
                    player_team = 1,
                    player_name = player_name,
                    match_number = match,
                    player_role = player_role
                )
                player.save()

        team2_select = request.POST.get('team2_select')
        team2_name = request.POST.get('team2_name')
        team2_coach = request.POST.get('team2_coach')
        team2_homeground = request.POST.get('team2_homeground')
        team2_select = 1 if team1_select == 'Team 1' else 2

        team2 = Team(
            team_name = team2_name,
            team_coach = team2_coach,
            team_homeground = team2_homeground,
            match_number = match,
            team_number = team2_select
        )
        team2.save()

        for i in range(1, 4):
            player_name = request.POST.get(f'player{i}_team2')
            player_role = request.POST.get(f'team2_player{i}_role')
            if player_name:
                player = Player(
                    player_team = 2,
                    player_name = player_name,
                    match_number = match,
                    player_role = player_role
                )
                player.save()

        return render(request, 'add_match.html')

    else:
        pass
    
    return render(request, 'add_match.html')
