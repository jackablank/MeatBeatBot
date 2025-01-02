from discord.ext import commands
import discord
from dotenv import load_dotenv
import os

def main():
    load_dotenv(dotenv_path='C:/MeatBeatBot/botkeys.env')
    botToken = os.getenv('BOT_TOKEN')

    BOT_TOKEN = "MTMyNDMwNjA1MTg1MTQ4NTIwNQ.GNjVpW.JYqWvedY0pPkvtqOOLjaX90qyARNFxmzH7TLXU"
    JERK_OFF_CHANNEL_ID = 1324309720026320978
    TEST_CHANNEL_ID = 1324309933239308300

    bot = commands.Bot(command_prefix='//', intents=discord.Intents.all())
    
    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')
        channel = bot.get_channel(TEST_CHANNEL_ID)
        await channel.send("jerk off time")

    @bot.command()
    async def add_phrase(ctx):
        await ctx.send("Phrase Added!")

    

    bot.run(botToken)


if __name__ == "__main__":
    main()