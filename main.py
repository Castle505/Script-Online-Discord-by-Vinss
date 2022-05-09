import discord, os, keep_alive, asyncio, datetime, pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=True
)



@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = "TANAH JAWA RP ┊ OPEN ADMIN OPEN ALL FACTION ┊ FRESH SERVER ┊ FAST RSPOND ┊ Vinss Store.", url = "https://www.twitch.tv/vinssstore"))


keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)
