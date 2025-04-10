from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)  # Replaced ObjectIdField with AutoField
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    members = models.ManyToManyField(User, related_name='teams')
    name = models.CharField(max_length=255)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_type = models.CharField(max_length=255)
    duration = models.IntegerField()
    calories_burned = models.IntegerField()
    date = models.DateField()
