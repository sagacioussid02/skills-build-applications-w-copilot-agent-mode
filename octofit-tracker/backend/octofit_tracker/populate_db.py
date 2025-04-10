from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email='user1@example.com', name='User One')
        user2 = User.objects.create(email='user2@example.com', name='User Two')

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')

        # Add users to teams
        team1.members.add(user1)
        team2.members.add(user2)

        # Create test activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2025-04-09')
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date='2025-04-08')

        # Create test leaderboard entries
        Leaderboard.objects.create(team=team1, score=100)
        Leaderboard.objects.create(team=team2, score=80)

        # Create test workouts
        Workout.objects.create(name='Morning Run', description='A quick morning run to start the day')
        Workout.objects.create(name='Evening Yoga', description='Relaxing yoga session in the evening')

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
