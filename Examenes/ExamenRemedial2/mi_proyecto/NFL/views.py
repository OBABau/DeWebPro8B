from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Stadium, Team, Player
from .forms import StadiumForm, TeamForm, PlayerForm


def home(request):
    """Home view that shows navigation to CRUD sections"""
    stadium_count = Stadium.objects.count()
    team_count = Team.objects.count()
    player_count = Player.objects.count()
    
    context = {
        'stadium_count': stadium_count,
        'team_count': team_count,
        'player_count': player_count,
    }
    return render(request, 'NFL/crud/home.html', context)


# Stadium CRUD Views
def stadium_list(request):
    stadiums = Stadium.objects.all()
    return render(request, 'NFL/crud/stadium_list.html', {'stadiums': stadiums})


def stadium_create(request):
    if request.method == 'POST':
        form = StadiumForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stadium created successfully!')
            return redirect('NFL:stadium_list')
    else:
        form = StadiumForm()
    return render(request, 'NFL/crud/stadium_form.html', {'form': form, 'title': 'Create Stadium'})


def stadium_update(request, pk):
    stadium = get_object_or_404(Stadium, pk=pk)
    if request.method == 'POST':
        form = StadiumForm(request.POST, instance=stadium)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stadium updated successfully!')
            return redirect('NFL:stadium_list')
    else:
        form = StadiumForm(instance=stadium)
    return render(request, 'NFL/crud/stadium_form.html', {'form': form, 'title': 'Update Stadium', 'stadium': stadium})


def stadium_delete(request, pk):
    stadium = get_object_or_404(Stadium, pk=pk)
    if request.method == 'POST':
        stadium.delete()
        messages.success(request, 'Stadium deleted successfully!')
        return redirect('NFL:stadium_list')
    return render(request, 'NFL/crud/stadium_confirm_delete.html', {'stadium': stadium})


def stadium_detail(request, pk):
    stadium = get_object_or_404(Stadium, pk=pk)
    teams = stadium.teams.all()
    return render(request, 'NFL/crud/stadium_detail.html', {'stadium': stadium, 'teams': teams})


# Team CRUD Views
def team_list(request):
    teams = Team.objects.select_related('stadium').all()
    return render(request, 'NFL/crud/team_list.html', {'teams': teams})


def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team created successfully!')
            return redirect('NFL:team_list')
    else:
        form = TeamForm()
    return render(request, 'NFL/crud/team_form.html', {'form': form, 'title': 'Create Team'})


def team_update(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team updated successfully!')
            return redirect('NFL:team_list')
    else:
        form = TeamForm(instance=team)
    return render(request, 'NFL/crud/team_form.html', {'form': form, 'title': 'Update Team', 'team': team})


def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        team.delete()
        messages.success(request, 'Team deleted successfully!')
        return redirect('NFL:team_list')
    return render(request, 'NFL/crud/team_confirm_delete.html', {'team': team})


def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    players = team.players.all()
    return render(request, 'NFL/crud/team_detail.html', {'team': team, 'players': players})


# Player CRUD Views
def player_list(request):
    players = Player.objects.select_related('team').all()
    return render(request, 'NFL/crud/player_list.html', {'players': players})


def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Player created successfully!')
            return redirect('NFL:player_list')
    else:
        form = PlayerForm()
    return render(request, 'NFL/crud/player_form.html', {'form': form, 'title': 'Create Player'})


def player_update(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            messages.success(request, 'Player updated successfully!')
            return redirect('NFL:player_list')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'NFL/crud/player_form.html', {'form': form, 'title': 'Update Player', 'player': player})


def player_delete(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        player.delete()
        messages.success(request, 'Player deleted successfully!')
        return redirect('NFL:player_list')
    return render(request, 'NFL/crud/player_confirm_delete.html', {'player': player})


def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'NFL/crud/player_detail.html', {'player': player})
