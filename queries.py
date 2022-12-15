import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("football.db")

# Define the query
query = """
SELECT Player.first_name, Player.last_name, Player.role, Player.age, Player.team_id, PlayerStat.qb_skill_index, PlayerStat.passing, PlayerStat.mobility, PlayerStat.game_reading, PlayerStat.team_leading
FROM Player
INNER JOIN PlayerStat ON Player.id = PlayerStat.player_id
WHERE Player.role = 'QB'
"""

# Execute the query
rows = conn.execute(query).fetchall()

df = pd.DataFrame(rows)

# Print the DataFrame
print(df)