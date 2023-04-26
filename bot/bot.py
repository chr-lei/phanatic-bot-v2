import os
from dotenv import load_dotenv
import discord
from api_queries import *
from datetime import datetime,timedelta

load_dotenv()

# Discord token
# TODO - Move this out of the environment file and set via CI/CD secret
TOKEN = os.getenv('DISCORD_TOKEN')
# Did My Team Win API URI
DMTW_API_URI = os.getenv('DMTW_API_URI')
# Team ID (numeric) that this bot will work with
# See https://github.com/chr-lei/phillies-win-api/blob/master/README.md
# for a list of Team names & IDs.
TEAMID = os.getenv('TEAMID')

# Set Discord Gateway Intents
intents = discord.Intents.all()

# Instantiate a Discord client and log in using token auth
client = discord.Client(command_prefix='!', intents=intents)

# Print a ready message after successful login
@client.event
async def on_ready():
    print("We're logged in as {0.user}".format(client))

# Set up a function to process channel messages
@client.event
async def on_message(message):
    content_lower = message.content.lower()
    # Ignore messages from the bot itself
    if message.author == client.user:
        return
    
    # Watch for a team name keyword
    # TODO - look for any keyword, match the team name to list,
    # and if match is found, run the code with a dynamic TeamId
    if "!phillies" in content_lower:
        print("Handling a message for user: %s; channel: %s; server: %s; content: %s" \
              %((message.author),(message.channel),(message.guild.name),(message.content)))
        #if "!yesterday" in content_lower:
        #    yesterday_date = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
        #    result = get_result(TEAMID,DMTW_API_URI,yesterday_date)
        #    await message.channel.send(result)
        #elif "!tomorrow" in content_lower:
        #    tomorrow_date = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
        #    result = get_result(TEAMID,DMTW_API_URI,tomorrow_date)
        #    await message.channel.send(result)
        result = get_result(TEAMID,DMTW_API_URI,(datetime.today()).strftime('%Y-%m-%d'))
        await message.channel.send(result)

# Run the bot
client.run(TOKEN)
