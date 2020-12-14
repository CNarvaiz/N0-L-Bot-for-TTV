import os

from twitchio.ext import commands
from twitchio import Client

#from time import time, timezone, altzone, localtime, daylight
from datetime import datetime, timedelta
from time import sleep


bot = commands.Bot(
	irc_token=os.environ['TMI_TOKEN'],
	client_id=os.environ['CLIENT_ID'],
	nick=os.environ['BOT_NICK'],
	prefix=os.environ['BOT_PREFIX'],
	initial_channels=[os.environ['CHANNEL']]
)

@bot.event
async def event_ready():
	print(f"{os.environ['BOT_NICK']} is online!")
	ws = bot._ws
	await ws.send_privmsg(os.environ['CHANNEL'], f"/me beeps cheerily as it comes online!")

@bot.event
async def event_message(ctx):
	if ctx.author.name.casefold() == os.environ['BOT_NICK'].casefold():
		return

	await bot.handle_commands(ctx)

	if 'hello' in ctx.content.casefold():
		await ctx.channel.send(f"Hi, @{ctx.author.name}!")

@bot.command(name='alive')
async def alive(ctx):
	await ctx.channel.send("Yes, I'm alive!")

@bot.command(name='lag')
async def lag(ctx):
	await ctx.channel.send("Lag? In DDO? You must have a bad connection, have you tried using wifi?")

@bot.command(name='info')
async def info(ctx):
	await ctx.channel.send("I am N0-L, Noelle's cheery helper-bot! I am written in python, hosted locally, and am currently still in development! Please be patient with me as my mom adds new functionality to my code!")

@bot.command(name='discord')
async def discord(ctx):
	await ctx.channel.send("Join us on discord and chat about stream, gaming, or anything else your sticky, nerdy heart desires! discord.gg/bmBMGKvDzb.")

@bot.command(name='guild')
async def guild(ctx):
	await ctx.channel.send("Join our Horde guild on Dawnbringer, 'Noelle's Nerd Pit'! For those not on Dawnbringer, we also have a Horde Community with auto-accept called 'Noelles Nerd Pit'!")

@bot.command(name='drg')
async def drg(ctx):
	await ctx.channel.send("Noelle mains Engineer, but plays any class that's needed for her groups! She usually hangs out in Drop Pod #247 in the stream's Discord, but is also sometimes in Pods #24 or #27 in the official DRG Discord!")
	await ctx.send("Any time there are open slots in Noelle's team, anyone is free to join the dig through Discord or Steam! Non-duplicate late joins is sometimes enabled, though!")
	await ctx.send("Rock and Stone!")

if __name__=="__main__":
	bot.run()