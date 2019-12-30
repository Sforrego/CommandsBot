# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import asyncio

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!corner ')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='send', help='Assigns corner role to member for duration minutes')
@commands.has_permissions(kick_members=True)
async def restrict(ctx, member:discord.Member, duration: int):
    role = discord.utils.get(ctx.guild.roles, name="Corner")
    await member.add_roles(role)
    name = member.nick if member.nick else member.name
    response = f"{name} has been sent to the corner for {duration} minutes."
    await ctx.send(response)
    await asyncio.sleep(duration*60)
    await member.remove_roles(role)


@bot.command(name='remove',help ='Removes Corner role from a specific member.')
@commands.has_permissions(kick_members=True)
async def remove_corners(ctx, member:discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Corner")
    await member.remove_roles(role)

@bot.command(name='reset', help ='Removes Corner role from every member.')
@commands.has_permissions(kick_members=True)
async def remove_corners(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Corner")
    for member in ctx.guild.members:
        await member.remove_roles(role)

@bot.command(name='members')
@commands.has_permissions(kick_members=True)
async def remove_corners(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Corner")
    members_in_corner = ''
    for member in ctx.guild.members:
        if role in member.roles:
            name = member.nick if member.nick else member.name
            members_in_corner += f'{name}\n'
    if members_in_corner == '':
        members_in_corner = 'No members in the corner.'
    await ctx.send(members_in_corner)



bot.run(token)


# @bot.command()
