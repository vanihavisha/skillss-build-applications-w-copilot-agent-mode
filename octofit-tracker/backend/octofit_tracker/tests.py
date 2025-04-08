from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(team.name, "Test Team")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email="test_activity@example.com", name="Activity User")
        activity = Activity.objects.create(user=user, description="Test Activity")
        self.assertEqual(activity.description, "Test Activity")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Leaderboard Team")
        leaderboard = Leaderboard.objects.create(team=team, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(email="test_workout@example.com", name="Workout User")
        workout = Workout.objects.create(user=user, type="Running", duration=30)
        self.assertEqual(workout.type, "Running")
