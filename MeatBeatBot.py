from discord.ext import commands
import discord
from dotenv import load_dotenv
import os
from datetime import datetime
import pytz

def main():
    load_dotenv(dotenv_path='C:/MeatBeatBot/botkeys.env')
    botToken = os.getenv('BOT_TOKEN')
    testChannelID = os.getenv('TEST_CHANNEL_ID')

    

    bot = commands.Bot(command_prefix='//', intents=discord.Intents.all())
    timezone = pytz.timezone("US/Pacific")

    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')
        channel = bot.get_channel(int(testChannelID))
        await channel.send("jerk off time")

    @bot.command()
    async def add_phrase(ctx):
        await ctx.send("Phrase Added!")

    @bot.listen()
    async def on_message(message):
        if message.author == bot.user:
            return
        if message.content == '@everyone jerking off':
            author = message.author
            timestamp = message.created_at

            localTime = timestamp.astimezone(timezone)
            formattedTime = localTime.strftime("%m/%d/%Y, %I:%M:%S %p %Z")

            await message.channel.send(f'🍆 User Beat Record Updated:\nUser Jerking It: {author}\nTimestamp: {formattedTime}')

    

    bot.run(botToken)


if __name__ == "__main__":
    main()