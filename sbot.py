import os, random, json, time
import random

import discord


def dump_file(file_name,arr):
    f=open(file_name, "r")
    arr = []
    for i in f.readlines():
        arr.append(i.strip())
    f.close()
    return arr

def write_file(file_name, arr):
    string=""
    f=open(file_name, "w")
    for i in arr:
        string+=i+"\n"

    f.write(string)
    f.close()

def generate_string(arr, amount):
    string = ""
    for i in range(amount):
        string+=random.choice(arr)
    
    return string
    

def load_json(file_name):
    with open(file_name, "r") as write_file:
        data = write_file.read()
        data = json.loads(data)
    return data



def dump_json(file_name, data):
    with open(file_name, "w") as write_file:
        json.dump(data, write_file)
       
def cler():
    print("\x1b[2J\x1b[H",end="")



random_words = []
random_words = dump_file("randomWords.txt", random_words)




TOKEN = 'NzIwNzIxODU2MTY0MDAzOTAy.XukkLQ.5DBEYqh92KowtOK1PvV7_gMyU1Y'

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="k, help"))
    
    print(f'{client.user} has connected to Discord!')






@client.event
async def on_message(message):
    
    if message.content == "":
        return


    if str(message.author) == "Kopamed#9408":
        
        await message.channel.send("MANIPULATING THE ANGLE OF THE BISECTOR OF THE MD5 HTML HASH TO THE CABLE OF THE BISECTING ROUTER::::::: HACKING IN PROGRESS")
client.run(TOKEN)