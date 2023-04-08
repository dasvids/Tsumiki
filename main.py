import settings
import discord
from discord.ext import commands


def run():
    intends = discord.Intents.default()
    
    bot = commands.Bot(command_prefix="!", intents=intends)

    @bot.event
    async def on_ready():
        print(f"{bot.user} has connected to Discord!")

    bot.run(settings.DISCORD_API_SECRET)


if __name__ == "__main__":
    run()
