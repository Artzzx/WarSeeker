import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from Warseeker.commands.admin.command import AdminCommands
from Warseeker.commands.force_link.command import force_link


intents = discord.Intents.all()
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")


bot = commands.Bot(command_prefix="/",intents =intents)

@bot.event
async def on_ready():
    print(f"[+] {bot.user.name} is now connected to Discord:\n")

@bot.event
async def on_disconnect():
    print(f'[-] {bot.user.name} has disconnected from Discord:\n')

@bot.event
async def on_resumed():
    print(f'[+] {bot.user.name} has resumed connection to Discord:\n')

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        return
    print(f'[-] An error has occured when running {ctx.command.name}:\n[-] Error: {error}')   



async def setup(bot:commands.bot):
   await bot.add_cog(AdminCommands(bot),guild=discord.Object(id=GUILD_ID))
   await bot.add_cog(force_link(bot),guild=discord.Object(id=GUILD_ID))
   print("[+] All cogs have been loaded successfully")

asyncio.run(setup(bot))
bot.run(TOKEN)