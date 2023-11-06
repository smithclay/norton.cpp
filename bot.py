import os
import logging

import asyncio
import discord
from llm import call
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class EmperorDiscordBot(discord.Client):
    """Discord bot for Emperor Norton I"""

    async def on_ready(self):
        """The Emperor is in court"""
        logging.info('Logged on as %s', self.user)

    async def on_message(self, message):
        """The Emperor has received a message"""

        if not self.should_reply(message):
            return

        async with message.channel.typing():
            output = await call(message.content)
            await message.channel.send(output)

    def should_reply(self, message):
        """Determine if The Emperor deigns to reply to a message"""
        if message.author == self.user:
            return False

        if isinstance(message.channel, discord.channel.DMChannel):
            return True

        for mention in message.mentions:
            if mention == self.user:
                return True

        for role in message.role_mentions:
            for member in role.members:
                if member == self.user:
                    return True
        return False


intents = discord.Intents.default()
intents.message_content = True
client = EmperorDiscordBot(intents=intents)
client.run(os.getenv('DISCORD_BOT_TOKEN'))
