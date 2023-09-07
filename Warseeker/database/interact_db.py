import sqlite3

# Function to insert player data and tags
def insert_player_data(discord_id, player_tags):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Insert player data (Discord ID)
    cursor.execute("INSERT INTO players (discord_id) VALUES (?)", (discord_id,))
    player_id = cursor.lastrowid  # Get the last inserted player ID

    # Insert player tags associated with the player
    for tag in player_tags:
        cursor.execute("INSERT INTO player_tags (player_id, player_tag) VALUES (?, ?)", (player_id, tag))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Function to query Discord ID by player tag(s)
def query_discord_id_by_player_tags(player_tags):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Create a comma-separated string of placeholders for the IN clause
    placeholders = ','.join(['?'] * len(player_tags))

    # Query the database to retrieve Discord IDs for the specified player tags
    query = f"SELECT player_tags.player_tag, players.discord_id FROM players JOIN player_tags ON players.player_id = player_tags.player_id WHERE player_tags.player_tag IN ({placeholders})"
    cursor.execute(query, player_tags)
    results = cursor.fetchall()

    # Create a dictionary to store the results with player tags as keys
    discord_id_by_player_tag = {row[0]: row[1] for row in results}

    # Close the connection
    conn.close()

    return discord_id_by_player_tag