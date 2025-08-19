from django.db import models


class Stadium(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    box_size = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name='teams')
    
    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    position = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    
    def __str__(self):
        return f"{self.name} - #{self.number}"
