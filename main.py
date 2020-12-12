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

#if u cant set this up, sorry to tell u but u r retarded
#aka add ur token in 'token' and in the discord channel run '>playercount'
