from django.contrib import admin
from .models import Stadium, Team, Player


@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity', 'box_size']
    search_fields = ['name']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'venue', 'owner_name', 'stadium']
    list_filter = ['stadium']
    search_fields = ['name', 'owner_name']


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'position', 'team']
    list_filter = ['position', 'team']
    search_fields = ['name', 'team__name']
