import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from .views import RoleSelectView


load_dotenv()
intents = discord.Intents.default()
bot = commands.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")
    bot.add_view(RoleSelectView(bot))


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


bot.run(os.environ.get('DISCORD_TOKEN'))
