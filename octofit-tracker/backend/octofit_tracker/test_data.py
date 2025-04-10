from datetime import datetime

# Sample data for the Octofit app
def get_test_data():
    return {
        "users": [
            {"id": 1, "username": "john_doe", "email": "john@example.com", "password": "password123"},
            {"id": 2, "username": "jane_smith", "email": "jane@example.com", "password": "password123"},
        ],
        "activities": [
            {"id": 1, "user_id": 1, "activity_type": "running", "duration": 30, "calories_burned": 300, "date": datetime(2025, 4, 10)},
            {"id": 2, "user_id": 2, "activity_type": "cycling", "duration": 45, "calories_burned": 400, "date": datetime(2025, 4, 9)},
        ],
        "teams": [
            {"id": 1, "name": "Team Alpha", "members": [1, 2]},
        ],
        "leaderboard": [
            {"user_id": 1, "points": 100},
            {"user_id": 2, "points": 120},
        ],
    }
