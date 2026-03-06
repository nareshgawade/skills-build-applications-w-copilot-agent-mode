"""
Script to populate the MongoDB database with test data for OctoFit Tracker
"""
import os
import django
from datetime import date, timedelta
import random

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard

def clear_database():
    """Clear existing data from all collections"""
    print("Clearing existing data...")
    Activity.objects.all().delete()
    Leaderboard.objects.all().delete()
    Workout.objects.all().delete()
    User.objects.all().delete()
    Team.objects.all().delete()
    print("Database cleared!")

def populate_teams():
    """Create test teams"""
    print("Creating teams...")
    teams = [
        Team.objects.create(
            name="The Octonauts",
            description="A team of octopus enthusiasts dedicated to fitness"
        ),
        Team.objects.create(
            name="Swift Swimmers",
            description="Water sports enthusiasts"
        ),
        Team.objects.create(
            name="Gym Warriors",
            description="Weight lifting and strength training team"
        ),
    ]
    print(f"Created {len(teams)} teams")
    return teams

def populate_users(teams):
    """Create test users"""
    print("Creating users...")
    users = [
        User.objects.create(
            name="Alice Johnson",
            email="alice@octofit.com",
            team=teams[0],
            is_superhero=True
        ),
        User.objects.create(
            name="Bob Smith",
            email="bob@octofit.com",
            team=teams[0],
            is_superhero=False
        ),
        User.objects.create(
            name="Charlie Brown",
            email="charlie@octofit.com",
            team=teams[1],
            is_superhero=False
        ),
        User.objects.create(
            name="Diana Prince",
            email="diana@octofit.com",
            team=teams[1],
            is_superhero=True
        ),
        User.objects.create(
            name="Eve Wilson",
            email="eve@octofit.com",
            team=teams[2],
            is_superhero=False
        ),
        User.objects.create(
            name="Frank Castle",
            email="frank@octofit.com",
            team=teams[2],
            is_superhero=True
        ),
    ]
    print(f"Created {len(users)} users")
    return users

def populate_activities(users):
    """Create test activities"""
    print("Creating activities...")
    activity_types = ['Running', 'Swimming', 'Cycling', 'Weight Training', 'Yoga', 'Hiking']
    activities = []
    
    for user in users:
        for i in range(5):
            activity = Activity.objects.create(
                user=user,
                type=random.choice(activity_types),
                duration=random.randint(30, 120),
                date=date.today() - timedelta(days=random.randint(0, 30))
            )
            activities.append(activity)
    
    print(f"Created {len(activities)} activities")
    return activities

def populate_workouts():
    """Create test workouts"""
    print("Creating workouts...")
    workouts = [
        Workout.objects.create(
            name="Morning Jog",
            description="A refreshing 5km morning jog for stamina building"
        ),
        Workout.objects.create(
            name="Power Hour",
            description="Intensive weight training session"
        ),
        Workout.objects.create(
            name="Swim & Relax",
            description="Swimming followed by stretching and relaxation"
        ),
        Workout.objects.create(
            name="Yoga Flow",
            description="Gentle yoga session for flexibility and mental health"
        ),
        Workout.objects.create(
            name="Cycling Challenge",
            description="Long distance cycling to build endurance"
        ),
    ]
    print(f"Created {len(workouts)} workouts")
    return workouts

def populate_leaderboards(teams):
    """Create leaderboard entries for teams"""
    print("Creating leaderboards...")
    leaderboards = []
    
    for team in teams:
        leaderboard = Leaderboard.objects.create(
            team=team,
            points=random.randint(100, 1000)
        )
        leaderboards.append(leaderboard)
    
    print(f"Created {len(leaderboards)} leaderboard entries")
    return leaderboards

def main():
    """Main function to run database population"""
    print("\n🏋️ Starting OctoFit Tracker Database Population...\n")
    
    try:
        clear_database()
        teams = populate_teams()
        users = populate_users(teams)
        activities = populate_activities(users)
        workouts = populate_workouts()
        leaderboards = populate_leaderboards(teams)
        
        print("\n✅ Database successfully populated with test data!")
        print(f"\nSummary:")
        print(f"  - Teams: {len(teams)}")
        print(f"  - Users: {len(users)}")
        print(f"  - Activities: {len(activities)}")
        print(f"  - Workouts: {len(workouts)}")
        print(f"  - Leaderboard Entries: {len(leaderboards)}")
        
    except Exception as e:
        print(f"\n❌ Error populating database: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
