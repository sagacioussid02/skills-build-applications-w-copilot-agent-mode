def get_test_data():
    return {
        "users": [
            {"id": 1, "username": "john_doe", "email": "john@example.com", "password": "password123"},
            {"id": 2, "username": "jane_doe", "email": "jane@example.com", "password": "password456"}
        ],
        "activities": [
            {"id": 1, "name": "Running", "calories_burned": 300, "user_id": 1},
            {"id": 2, "name": "Cycling", "calories_burned": 250, "user_id": 2}
        ],
        "teams": [
            {"id": 1, "name": "Team Alpha", "members": [1, 2]},
            {"id": 2, "name": "Team Beta", "members": []}
        ],
        "leaderboard": [
            {"id": 1, "team": 1, "points": 100, "user_id": 1},
            {"id": 2, "team": 2, "points": 50, "user_id": 2}
        ],
        "workouts": [
            {"id": 1, "name": "Morning Run", "duration": 30},
            {"id": 2, "name": "Evening Yoga", "duration": 45}
        ]
    }
