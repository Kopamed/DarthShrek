import os
import random
import os, random, json, time
import random

import discord

# 1
from discord.ext import commands


TOKEN = 'NzIwNzIxODU2MTY0MDAzOTAy.Xvs2eQ.Fb_SI2OXm_2HGkIxyDOZUTWo0rs'

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')



@bot.command(name='test', help="Gives you an investment message")
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        "You have invested $500. You lost 14%. You got back $430. You lost $70"
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)




@bot.command(name='rollDice', help='Simulates rolling dice.')
async def roll(ctx, number_of_sides, number_of_dice):
    dice = [
        str(random.randint(1, int(number_of_sides)))for i in range(int(number_of_dice))
    ]
    await ctx.send(', '.join(dice))
    
    
    
    
@bot.command(name='create-channel', help="CReates a channel")
@commands.has_role('Admin')
async def create_channel(ctx, channel_name):
    guild = ctx.guild
    print("her")
    try:
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        
    except:
        print("Here")
        
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)
        
    
    
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


bot.run(TOKEN)