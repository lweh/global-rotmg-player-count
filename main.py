#run 'pip install discord'
import discord
from datetime import datetime
import requests
from discord.ext import commands

client = commands.Bot(command_prefix=">")
playcoun = requests.get("https://realmstock.network/public/playersonline")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

@client.event
async def on_ready():
	print("Ready!")

@client.command(aliases=['playercount'])
async def rule(ctx):
	print(f">> {playcoun.text}")
	#change (UK) to whatever timezone ur in
	await ctx.send(f"[(UK) {current_time}] Players Online: {playcoun.text} \nCredits to RealmStock and Jakub!")

client.run("token")


#this is the simplest bot a human can do, therefore no readme, if u cant set this up ur mentally handicapped
