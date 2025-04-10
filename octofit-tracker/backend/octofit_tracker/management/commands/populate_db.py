from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import get_test_data

def populate_database():
    test_data = get_test_data()

    # Populate users
    for user_data in test_data['users']:
        User.objects.update_or_create(
            id=user_data['id'],
            defaults={
                'email': user_data['email'],
                'name': user_data['username']
            }
        )

    # Populate teams
    for team_data in test_data['teams']:
        team, created = Team.objects.update_or_create(
            id=team_data['id'],
            defaults={'name': team_data['name']}
        )
        team.members.set(team_data['members'])

    # Populate activities
    for activity_data in test_data['activities']:
        Activity.objects.update_or_create(
            id=activity_data['id'],
            defaults={
                'user_id': activity_data['user_id'],
                'activity_type': activity_data['name'],
                'duration': activity_data.get('duration', 0),
                'date': activity_data.get('date', '2025-04-10')  # Default to current date if missing
            }
        )

    # Populate leaderboard
    for leaderboard_data in test_data['leaderboard']:
        Leaderboard.objects.update_or_create(
            id=leaderboard_data['id'],
            defaults={
                'team_id': leaderboard_data['team'],
                'score': leaderboard_data['points']
            }
        )

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        populate_database()
        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
