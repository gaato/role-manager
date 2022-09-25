import os
import pathlib

import discord
from dotenv import load_dotenv

from ..views import SelectView1
from .. import config


HERE = pathlib.Path(__file__).parent

load_dotenv()
intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("------")
    button_channel = client.get_channel(config.select_channel_id)
    view = SelectView1(client)
    message = await button_channel.send('ご自身の役割を以下から選んでください。', view=view)
    print(f'BUTTON_MESSAGE_ID = {message.id}')
    await client.close()


client.run(os.environ.get('DISCORD_TOKEN'))
