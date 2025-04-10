import sqlite3
from test_data import get_test_data

def populate_database():
    # Connect to the database
    conn = sqlite3.connect('octofit_db.sqlite3')
    cursor = conn.cursor()

    # Get test data
    test_data = get_test_data()

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, email TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS activities (id INTEGER PRIMARY KEY, name TEXT, calories_burned INTEGER)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS teams (id INTEGER PRIMARY KEY, name TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS team_members (team_id INTEGER, user_id INTEGER, FOREIGN KEY(team_id) REFERENCES teams(id), FOREIGN KEY(user_id) REFERENCES users(id))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS leaderboard (id INTEGER PRIMARY KEY, team INTEGER, points INTEGER, FOREIGN KEY(team) REFERENCES teams(id))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS workouts (id INTEGER PRIMARY KEY, name TEXT, duration INTEGER)''')

    # Insert data into users table
    for user in test_data['users']:
        cursor.execute('INSERT OR IGNORE INTO users (id, username, email) VALUES (?, ?, ?)', (user['id'], user['username'], user['email']))

    # Insert data into activities table
    for activity in test_data['activities']:
        cursor.execute('INSERT OR IGNORE INTO activities (id, name, calories_burned) VALUES (?, ?, ?)', (activity['id'], activity['name'], activity['calories_burned']))

    # Insert data into teams table
    for team in test_data['teams']:
        cursor.execute('INSERT OR IGNORE INTO teams (id, name) VALUES (?, ?)', (team['id'], team['name']))
        for member_id in team['members']:
            cursor.execute('INSERT OR IGNORE INTO team_members (team_id, user_id) VALUES (?, ?)', (team['id'], member_id))

    # Insert data into leaderboard table
    for entry in test_data['leaderboard']:
        cursor.execute('INSERT OR IGNORE INTO leaderboard (id, team, points) VALUES (?, ?, ?)', (entry['id'], entry['team'], entry['points']))

    # Insert data into workouts table
    for workout in test_data['workouts']:
        cursor.execute('INSERT OR IGNORE INTO workouts (id, name, duration) VALUES (?, ?, ?)', (workout['id'], workout['name'], workout['duration']))

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    populate_database()
