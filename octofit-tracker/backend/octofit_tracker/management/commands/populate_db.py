from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import get_test_data

def populate_database():
    test_data = get_test_data()

    # Populate users
    for user_data in test_data['users']:
        User.objects.create(
            id=user_data['id'],
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password']
        )

    # Populate teams
    for team_data in test_data['teams']:
        team = Team.objects.create(
            id=team_data['id'],
            name=team_data['name']
        )
        team.members.set(team_data['members'])

    # Populate activities
    for activity_data in test_data['activities']:
        Activity.objects.create(
            id=activity_data['id'],
            user_id=activity_data['user_id'],
            activity_type=activity_data['activity_type'],
            duration=activity_data['duration'],
            calories_burned=activity_data['calories_burned'],
            date=activity_data['date']
        )

    # Populate leaderboard
    for leaderboard_data in test_data['leaderboard']:
        Leaderboard.objects.create(
            user_id=leaderboard_data['user_id'],
            points=leaderboard_data['points']
        )

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        populate_database()
        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
