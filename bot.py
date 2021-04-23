from discord.ext import commands, tasks
from itertools import cycle
from tinydb import *
from colorama import Fore, Back, Style

import discord
import colorama
import requests
import json
import time
import os

os.system('cls')
authenticity_token = 'ODMyNjU2ODk2NDQ3NzQxOTc0.YHm-Kg.Ss2tMHtIDX1zKcYbIOB0yQWVlLE'
client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("Bot ready.")
    client.User = Query()
    client.db = TinyDB('vouches.json')

@client.command(name="vouch")
async def vouch(context, args : discord.Member):

    client.db.insert({'name': str(args.id), 'vouches' : 0,'vouchby':str(context.message.author.id)})

    await context.send("Vouched.")

@client.command(name="rep")
async def rep(context, args : discord.Member):

    vouchesofuser = client.db.search(client.User.name == str(args.id))

    embed = discord.Embed(title="Vouches", description=str(args.id) + " has " + str(len(vouchesofuser)) + " vouches.", color=0x00ff39)
    await context.send(embed=embed)

@client.command(name="vouches")
async def vouches(context, args : discord.Member):

    list_name = []
    result = client.db.search(client.User.name == str(args.id))

    for name in result:
        listtoappend = f"<@{name['vouchby']}>"
        list_name.append(listtoappend)

    embed = discord.Embed(title=f"Vouches of {str(args)}", description=', '.join(list_name ), color=0x00d9ff)
    await context.send(embed=embed)























def run():
    client.run('ODMyNjU2ODk2NDQ3NzQxOTc0.YHm-Kg.Ss2tMHtIDX1zKcYbIOB0yQWVlLE')

run() 