from django import forms
from .models import Stadium, Team, Player


class StadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = ['name', 'capacity', 'box_size']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-bordered w-full', 'placeholder': 'Stadium name'}),
            'capacity': forms.NumberInput(attrs={'class': 'input input-bordered w-full', 'placeholder': 'Capacity'}),
            'box_size': forms.TextInput(attrs={'class': 'input input-bordered w-full', 'placeholder': 'Box size'}),
        }


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'venue', 'owner_name', 'stadium']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-bordered w-full', 'placeholder': 'Team name'}),
            'venue': forms.TextInput(attrs={'class': 'input input-bordered w-full', 'placeholder': 'Venue location'}),
            'owner_name': forms.TextInput(attrs={'class': 'input input-bordered w-full', 'placeholder': 'Owner name'}),
            'stadium': forms.Select(attrs={'class': 'select select-bordered w-full'}),
        }


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'number', 'position', 'team']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-bordered w-full', 'placeholder': 'Player name'}),
            'number': forms.NumberInput(attrs={'class': 'input input-bordered w-full', 'placeholder': 'Player number'}),
            'position': forms.TextInput(attrs={'class': 'input input-bordered w-full', 'placeholder': 'Position'}),
            'team': forms.Select(attrs={'class': 'select select-bordered w-full'}),
        }
