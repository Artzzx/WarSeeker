import discord
import os
import asyncio
from discord.ext import commands

intents = discord.Intents.all()

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
   # await bot.add_cog(Apply(bot),guild=discord.Object(id=GUILD_ID))
   pass

asyncio.run(setup(bot))
bot.run(TOKEN)