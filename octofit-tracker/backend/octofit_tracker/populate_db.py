from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Activity, Team, Leaderboard, Workout
from octofit_tracker.test_data import get_test_data

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        test_data = get_test_data()

        # Populate users
        for user_data in test_data['users']:
            User.objects.get_or_create(**user_data)

        # Populate activities
        for activity_data in test_data['activities']:
            Activity.objects.get_or_create(**activity_data)

        # Populate teams
        for team_data in test_data['teams']:
            team, created = Team.objects.get_or_create(id=team_data['id'], name=team_data['name'])
            team.members.set(team_data['members'])

        # Populate leaderboard
        for leaderboard_data in test_data['leaderboard']:
            Leaderboard.objects.get_or_create(**leaderboard_data)

        # Populate workouts
        for workout_data in test_data.get('workouts', []):
            Workout.objects.get_or_create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
