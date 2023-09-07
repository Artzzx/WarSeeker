import sqlite3

# Function to create the database and tables
def create_database():
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Create a table for player data
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS players (
           player_id INTEGER PRIMARY KEY AUTOINCREMENT,
           discord_id TEXT NOT NULL
       )
    ''')
    print("created table players")

    # Create a table for player tags, linking them to the player
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS player_tags (
           tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
           player_id INTEGER NOT NULL,
           player_tag TEXT NOT NULL,
           FOREIGN KEY (player_id) REFERENCES players (player_id)
       )
    ''')
    print("created table player_tags")

    # Commit changes and close the connection
    conn.commit()
    conn.close()

create_database()
