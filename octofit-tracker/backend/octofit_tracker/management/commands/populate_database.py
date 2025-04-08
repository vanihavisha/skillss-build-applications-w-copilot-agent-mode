from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data in the correct order
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.filter(id__isnull=False).delete()
        User.objects.all().delete()

        # Save teams with valid primary keys
        team1 = Team.objects.create(name='Blue Team')
        team2 = Team.objects.create(name='Gold Team')

        # Create users
        users = [
            User(id=ObjectId(), email='thundergod@mhigh.edu', name='Thor'),
            User(id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark'),
            User(id=ObjectId(), email='zerocool@mhigh.edu', name='Steve Rogers'),
            User(id=ObjectId(), email='crashoverride@mhigh.edu', name='Natasha Romanoff'),
            User(id=ObjectId(), email='sleeptoken@mhigh.edu', name='Bruce Banner'),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user=users[0], description='Cycling', timestamp='2025-04-08T10:00:00Z'),
            Activity(user=users[1], description='Crossfit', timestamp='2025-04-08T11:00:00Z'),
            Activity(user=users[2], description='Running', timestamp='2025-04-08T12:00:00Z'),
            Activity(user=users[3], description='Strength Training', timestamp='2025-04-08T13:00:00Z'),
            Activity(user=users[4], description='Swimming', timestamp='2025-04-08T14:00:00Z'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team1, score=100),
            Leaderboard(team=team2, score=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(user=users[0], type='Cycling', duration=60),
            Workout(user=users[1], type='Crossfit', duration=120),
            Workout(user=users[2], type='Running', duration=90),
            Workout(user=users[3], type='Strength Training', duration=30),
            Workout(user=users[4], type='Swimming', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))