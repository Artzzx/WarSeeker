import discord
from discord.ext import commands
from discord import app_commands
from Warseeker.database.interact_db import insert_player_data
import traceback
import sqlite3

class force_link(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="force_link")
    async def cmd_apply(self, interaction: discord.Interaction, member: discord.Member, player_tag1: str, player_tag2: str = None, player_tag3: str = None, player_tag4: str = None, player_tag5: str = None):
        """Add a player tag to the database. Done by admin only."""
        if "owner" not in [role.name.lower() for role in member.roles]:
            await interaction.response.send_message("command not authorized")
            return
        # Connect to the SQLite database
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        try:
            # Get the Discord ID of the member
            discord_id = str(member.id)

            # Insert or update the mandatory player tag (player_tag1)
            if player_tag1:
                insert_player_data(discord_id, [player_tag1])

            # Insert optional player tags (player_tag2 to player_tag5)
            optional_tags = [tag for tag in [player_tag2, player_tag3, player_tag4, player_tag5] if tag]
            if optional_tags:
                insert_player_data(discord_id, optional_tags)

            await interaction.response.send_message(f"Successfully updated {member} player tag in the database.")

        except Exception as e:
            print(e)
            await interaction.response.send_message("An error occurred while updating the database.")
