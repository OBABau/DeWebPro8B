from django.urls import path
from . import views

app_name = 'NFL'

urlpatterns = [
    path('', views.home, name='home'),
    
    # Stadium CRUD URLs
    path('stadiums/', views.stadium_list, name='stadium_list'),
    path('stadiums/create/', views.stadium_create, name='stadium_create'),
    path('stadiums/<int:pk>/', views.stadium_detail, name='stadium_detail'),
    path('stadiums/<int:pk>/update/', views.stadium_update, name='stadium_update'),
    path('stadiums/<int:pk>/delete/', views.stadium_delete, name='stadium_delete'),
    
    # Team CRUD URLs
    path('teams/', views.team_list, name='team_list'),
    path('teams/create/', views.team_create, name='team_create'),
    path('teams/<int:pk>/', views.team_detail, name='team_detail'),
    path('teams/<int:pk>/update/', views.team_update, name='team_update'),
    path('teams/<int:pk>/delete/', views.team_delete, name='team_delete'),
    
    # Player CRUD URLs
    path('players/', views.player_list, name='player_list'),
    path('players/create/', views.player_create, name='player_create'),
    path('players/<int:pk>/', views.player_detail, name='player_detail'),
    path('players/<int:pk>/update/', views.player_update, name='player_update'),
    path('players/<int:pk>/delete/', views.player_delete, name='player_delete'),
]
