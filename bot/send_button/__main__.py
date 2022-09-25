import os
import pathlib

import discord
from dotenv import load_dotenv

from ..views import ButtonView1
from .. import config


HERE = pathlib.Path(__file__).parent

load_dotenv()
intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("------")
    button_channel = client.get_channel(config.button_channel_id)
    view = ButtonView1(client)
    await button_channel.send(f'Please read <#{config.rule_channel_id}> carefully and press the button below.\n<#{config.rule_channel_id}>をよく読んで以下のボタンを押してください。', view=view)
    await client.close()


client.run(os.environ.get('DISCORD_TOKEN'))
