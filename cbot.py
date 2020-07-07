import os, random, json, time
import random

import discord

import gspread, random, json, time
from oauth2client.service_account import ServiceAccountCredentials


        

class Database:
    
    def __init__(self, url, name, worksheet_name):
        self.url = url
        self.name = name
        self.worksheet_name = worksheet_name
        self.count = 0
        self.n=3
        
        self.gc = gspread.service_account(filename="client_secret.json")
        self.sh = self.gc.open_by_url(self.url).worksheet(self.worksheet_name)
        
        self.gc1 = gspread.service_account(filename="client_secret1.json")
        self.sh1 = self.gc1.open_by_url(self.url).worksheet(self.worksheet_name)
    
        self.gc2 = gspread.service_account(filename="client_secret2.json")
        self.sh2 = self.gc2.open_by_url(self.url).worksheet(self.worksheet_name)
        
        self.gc3 = gspread.service_account(filename="client_secret3.json")
        self.sh3 = self.gc3.open_by_url(self.url).worksheet(self.worksheet_name)
        
        #self.gc = gspread.service_account(filename="client_secret.json")
        #self.sh = self.gc.open_by_url(self.url).worksheet(self.worksheet_name)
        
        #self.gc = gspread.service_account(filename="client_secret.json")
        #self.sh = self.gc.open_by_url(self.url).worksheet(self.worksheet_name)
        
        #self.gc = gspread.service_account(filename="client_secret.json")
        #self.sh = self.gc.open_by_url(self.url).worksheet(self.worksheet_name)
        
        #self.gc = gspread.service_account(filename="client_secret.json")
        #self.sh = self.gc.open_by_url(self.url).worksheet(self.worksheet_name)
        
        #self.gc = gspread.service_account(filename="client_secret.json")
        #self.sh = self.gc.open_by_url(self.url).worksheet(self.worksheet_name)
        
        #self.gc = gspread.service_account(filename="client_secret.json")
        #self.sh = self.gc.open_by_url(self.url).worksheet(self.worksheet_name)
        
        #self.gc = gspread.service_account(filename="client_secret.json")
        #self.sh = self.gc.open_by_url(self.url).worksheet(self.worksheet_name)
        
        #self.gc = gspread.service_account(filename="client_secret.json")
        #self.sh = self.gc.open_by_url(self.url).worksheet(self.worksheet_name)
    
    def load_json(self,file_name):
        
        with open(file_name, "r") as write_file:
            data = write_file.read()
            data = json.loads(data)
            
        return data



    def dump_json(self,file_name, data):
        
        with open(file_name, "w") as write_file:
            json.dump(data, write_file)



    def push(self, arr):
        
        y = len(self.sh.col_values(1))+1
        for i in range(len(arr)):
            
            if self.count == 0:
                self.sh.update_cell(y, i+1, arr[i])
            
            elif self.count == 1:
                self.sh1.update_cell(y, i+1, arr[i])
                
            elif self.count == 2:
                self.sh2.update_cell(y, i+1, arr[i])    
                
            elif self.count == 3:
                self.sh3.update_cell(y, i+1, arr[i])
                
                
            if self.count == self.n:
                self.count = 0
            else:
                self.count += 1
                
            
        
    



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




TOKEN = 'NzIwNzIxODU2MTY0MDAzOTAy.XvukOQ.jsrisJXGGmoaDmCl7DUAFfBZS8k'

client = discord.Client()
print("LOading Database...")
database = Database("https://docs.google.com/spreadsheets/d/1RKOzsosgbyMX8Cgk6O59xs5y5Ki2LZAr3HL6YsYoZ3I/edit#gid=0", "messages", "Sheet1")
print("done")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your mum || k, help"))
    
    print(f'{client.user} has connected to Discord!')



@client.event
async def on_member_join(member):

    expected = generate_string(random_words, 5)

    userInfo = load_json("userInfo.json")
    
    userInfo[str(member)] = {"password": expected, "points": 0, "messages": 0,"trusted": False}
    
    dump_json("userInfo.json", userInfo)
    userInfo = load_json("userInfo.json")
    
    await member.add_roles(member.guild.get_role(721253913201999912) , reason="User Trusted", atomic=True)
    
    
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.mention}, welcome to The Gaming Sever! *YOU HAVE TO READ THE RULES BEFORE JOINING THE SERVER!*\n*HERE ARE THE RULES: \n-------------\n1. No Spamming or kick\n2. Swearing is allowed but keep it minimal\n3.  No starting conflicts\n4. Don`t be an asshole\n5. No toxicity\n6. No racist or homophobic comments (or ban)\n7. No pornography/hentai or any sexual content\n10. To be allowed to proceed, type {expected} in the server (where MEE6 mentioned you)\n---------------*\nWe hope you have a great time here!\n(If you need help, tag @Helper on the server)'
    )
    channel = member.guild.get_channel(722872295072333864)
    
    dir = 'Memes'
    filename = random.choice(os.listdir(dir))
    path = os.path.join(dir, filename)
    file = discord.File(path, filename=filename)
    embed = discord.Embed(title=f"{member} just joined the server!", colour = 0xffa500)
                
    embed.set_image(url=f"attachment://{filename}")
                
    await channel.send(content = "<@!707443953028431904>", file=file, embed=embed)
                
   
@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.id == 725252266738581584:
        await user.add_roles(user.guild.get_role(725250901761327134) , reason="YT", atomic=True)
        
@client.event
async def on_reaction_remove(reaction, user):
    if reaction.message.id == 725252266738581584:
        await user.remove_roles(user.guild.get_role(725250901761327134) , reason="YT", atomic=True)
        
        


@client.event
async def on_message(message):
    
    if message.content == "":
        return
    #count = 0
    ##for i in message.guild.members:
    #    count+=1
    #    cler()
    #    print(f"{round(count/len(message.guild.members)*100,2)}% - {count} / {len(message.guild.members)}")
    #    print(f"changing roles for {i}")
    #    await i.add_roles(message.guild.get_role(722835345871470682),reason="User Trusted", atomic=True)
    #    await i.remove_roles(message.guild.get_role(714561606486589531),reason="User Trusted", atomic=True)
        
    
    
    settings = load_json("settings.json")
    user_info = load_json("userInfo.json")
    message_history = load_json("messages.json")
    
    #user_info[str(message.author)]["messages"] +=1
        
        
    
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    print(f"{current_time} - {message.channel} - {message.author} - {message.content}")
    
    message_history.append({"ftime": time.time(),"time": str(current_time), "guild": str(message.guild), "channel": str(message.channel), "author": str(message.author), "content": str(message.content)})
    

    strings = time.strftime("%d,%m, %Y")
    t = strings.split(',')
    numbers = [ int(x) for x in t ]
    now="/".join(str(i) for i in numbers)
    database.push([now, time.time(), str(current_time), str(message.guild), str(message.channel), str(message.author), str(message.content)])
    
    dump_json("messages.json", message_history)
    dump_json("userInfo.json", user_info)
    
    
    if settings["flags"]["ignoreBots"] and message.author == client.user:
        return
    
    
    
    ######################
    
    if len(message.content.split()) >= 2 and message.content.split()[0] == "k," and message.content.split()[1] == "flag":
        if str(message.author.top_role) in settings["opRanks"]:
            if message.content == "k, flag":
                print("Here")
                embed = discord.Embed(title="Available flags", colour=0x63ebe4)
                for i in settings["flags"]:
                    embed.add_field(name=i, value=settings["flags"][i])
                await message.channel.send(content=None, embed=embed)

            if len(message.content.split()) == 3:
            
                if message.content.split()[2] in settings["flags"]:
                    
                    await message.channel.send(str(settings["flags"][message.content.split()[2]])) 

                else:
                    await message.channel.send(f"There is no such flag named [{message.content.split()[2]}]")

            elif len(message.content.split()) == 4:
                if message.content.split()[2] in settings["flags"]:

                    if message.content.split()[3].lower() == "true":
                        settings["flags"][message.content.split()[2]] = True
                        
                        await message.channel.send(f"Updated {message.content.split()[2]} to {settings['flags'][message.content.split()[2]]}")

                    elif message.content.split()[3].lower() == "false":
                        settings["flags"][message.content.split()[2]] = False
                        await message.channel.send(f"Updated {message.content.split()[2]} to {settings['flags'][message.content.split()[2]]}")

                    else:
                        await message.channel.send(f"{message.content.split()[3]} is not a boolean")
                else:
                    await message.channel.send(f"There is no such flag named [{message.content.split()[2]}]")
        else:
            embed = discord.Embed(title="Permission Error", colour = 0xff0000)
            embed.add_field(name="Error", value="You do not have the permision to do this!") 
            await message.channel.send(content=None, embed = embed)
        dump_json("settings.json", settings)
        
        
        ##############################3
   



    if settings["flags"]["addComments"]:
        if message.content.find("gg") != -1:
            await message.channel.send("gg")    
        
        
        elif "f" in message.content.lower().split() or "fs" in message.content.lower():
            response = "f"
            await message.channel.send(response)



    if settings["flags"]["controlWelcome"]:
        if message.channel.id == 713878094062157920:
            try:
                user_info = load_json("userInfo.json")
                if user_info[str(message.author)]["trusted"] == False:
                    if user_info[str(message.author)]["password"] in message.content.lower():
                        embed = discord.Embed(title="User Accepted", colour = 0x00ff00)
                        embed.add_field(name="User Accpeted", value="You now have access to the rest of the server. Have fun! DO NOT USE THIS CHANNEL ANYMORE OR YOU WILL GET A WARNING")
                        
                        await message.author.add_roles(message.guild.get_role(722835345871470682) , reason="User Trusted", atomic=True)
                        
                        await message.author.remove_roles(message.guild.get_role(721253913201999912) , reason="User Trusted", atomic=True)
                        user_info[str(message.author)]["trusted"] = True
                        dump_json("userInfo.json", user_info)
                        await message.channel.send(content=None, embed = embed)
                    
                    else:
                        if message.author.bot != True and str(message.author) != "Godgamer123#6997" and str(message.author) != "Kopamed#9408":
                        
                            embed = discord.Embed(title="Incorrect Password",colour = 0xff0000)
                            embed.add_field(name="Incorrect Password", value="You have made a mistake while typing out the keywords") 
                            await message.channel.send(content=None, embed = embed)
        
                else:
                    if str(message.author) != "Kopamed#9408":
                        embed = discord.Embed(title="Protocol Breached",colour = 0xff0000)
                        embed.add_field(name="Protocol Breached", value="You have used this channel without permission. You will noww recieve a warning!") 
                        await message.channel.send(content=None, embed = embed)
            except Exception as e:
                
                embed = discord.Embed(title="Error69-420", colour = 0xff0000)
                embed.add_field(name="Database Error", value=f"An error has occured in our database. Try leaving the server and re-joining it. {Dev.mention}, here is the error: {e}")
                await message.channel.send(content=None, embed = embed) 
        
        
    if settings["flags"]["botEnabled"]:
        if message.content == "k, help":
            if str(message.author.top_role) in settings["opRanks"]:
                embed = discord.Embed(title="Command prefix = k,", colour = 0xffa500)
                embed.add_field(name="shoutout", value="Shouts out a random person")
                embed.add_field(name="echo", value="The bot says something. Type *k, echo* for more info")
                embed.add_field(name="rnum", value="Gives you a random number. Type k, rnum for more info")
                embed.add_field(name="users", value="Shows the amount of users there are in the server")
                embed.add_field(name="flag", value="Shows all the flags. You can modify flags with k, flag [flagName] [true ot false]")
                embed.add_field(name="meme", value="Shows you a meme")
                embed.add_field(name="8ball", value="Ask the magic 8ball something that you don't know and it will tell you the truth")
                embed.add_field(name="ping", value="You can ping anyone and the bot will delete the message immediatly. No one will ever know it was you. k, ping [@user]")
                embed.add_field(name="Earnable ranks", value="This is not a command but there is a 0.01% that you will recive a special role when doing __**k, meme**__!")
                await message.channel.send(content=None, embed = embed)
                
            else:
                embed = discord.Embed(title="Command prefix = k,", colour = 0xffa500)
                embed.add_field(name="rnum", value="Gives you a random number. Type k, rnum for more info")
                embed.add_field(name="users", value="Shows the amount of users there are in the server")
                embed.add_field(name="meme", value="Shows you a meme")
                embed.add_field(name="8ball", value="Ask the magic 8ball something that you don't know and it will tell you the truth")
                embed.add_field(name="Earnable ranks", value="This is not a command but there is a 0.01% that you will recive a special role when doing __**k, meme**__!")
                await message.channel.send(content=None, embed = embed)
                
                        

            
        
        elif message.content.split()[0] == "k," and len(message.content.split()) >= 2:
            
            if message.content.split()[1] == "shoutout":
                if str(message.author.top_role) in settings["opRanks"]:
                    if len(message.content.split()) == 2:
                        user = random.choice(message.guild.members)
                        await message.channel.send(user.mention)
                    
                else:
                    embed = discord.Embed(title="Permission Error", colour = 0xff0000)
                    embed.add_field(name="Error", value="You do not have the permision to do this!") 
                    await message.channel.send(content=None, embed = embed)
                   
            
            elif "echo" == message.content.split()[1]:
                if str(message.author.top_role) in settings["opRanks"]:
                    split_message = message.content.split()
                    r_channels= {}
                    for i in message.guild.channels:
                        r_channels[str(i)] = i.id
                        
                    if len(split_message) >= 3:
                    #if len(split_message)
                        if split_message[2] in r_channels:
                            
                            message.channel = client.get_channel(r_channels[split_message[2]])
                            try:
                                for i in range(int(split_message[3])):
                                    start = len(split_message[0])+len(split_message[1])+len(split_message[2])+len(split_message[3])+4
                                    print(start)
                                    response = message.content[start:]
                                    await message.channel.send(response)
                                    print(f"{message.author} made {client.user} say {response} in {message.channel} {split_message[3]} times")
                            except:
                                start = len(split_message[0])+len(split_message[1])+len(split_message[2])+3
                                response = message.content[start:]
                                await message.channel.send(response)
                                print(f"{message.author} made {client.user} say {response} in {message.channel}")
                        else:
                            start = len(split_message[0])+len(split_message[1])+2
                            response = message.content[start:]
                            await message.channel.send(response)
                            print(f"{message.author} tried to make {client.user} say {response} in {split_message[2]}")
                    
                    else:
                        embed = discord.Embed(title="How to use k, echo", colour = 0xffa500)
                        embed.add_field(name="Simple", value="The bot will repet what you say. E.g. *k, echo I will repeat this* (output: I will repeat this)")
                        embed.add_field(name="Advanced", value="The bot will repet what you say in a channel of your choice. E.g. *k, echo 💬main-chat💬 I will repeat this* (output: I will repeat this)")
                        embed.add_field(name="Advanced", value="The bot will repet what you say in a channel of your choice a certain number of times. E.g. *k, echo 💬main-chat💬 10 I will repeat this* (output: I will repeat this)")
                        await message.channel.send(content=None, embed = embed)
                        
                        
                else:
                    embed = discord.Embed(title="Permission Error", colour = 0xff0000)
                    embed.add_field(name="Error", value="You do not have the permision to do this!") 
                    await message.channel.send(content=None, embed = embed)
        
            
            elif message.content.split()[1] == "meme":
            
            

                dir = 'Memes'
                filename = random.choice(os.listdir(dir))
                path = os.path.join(dir, filename)
                file = discord.File(path, filename=filename)
                embed = discord.Embed(title="Here ya go:", colour = 0xffa500)
                
                embed.set_image(url=f"attachment://{filename}")
                
                await message.channel.send(file=file, embed=embed)
                if random.randint(0,10000) == 14:
                    allow = True
                    for i in message.author.roles:
                        if i.id == 714828598955212865:
                            allow= False
                    if allow == True:
                        await message.author.add_roles(message.guild.get_role(714828598955212865) , reason="Lucky...", atomic=True)
                        await message.channel.send(f"Congrats {message.author.mention}! You have just won your self a Lucky Memer Rank! There is only a 0.01% chance of you getting one of these ranks so do feel lucky. Congrats! (Btw, i love memes too <3)")
                    
                
            elif message.content.split()[1] == "8ball":
            
                r_answers = ["As I see it, yes", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don’t count on it", "It is certain", "It is decidedly so", "Most likely", "My reply is no", " My sources say no", "Outlook not so good", "Outlook good", "Reply hazy, try again", "Signs point to yes", "Very doubtful", "Without a doubt","Yes", "Yes – definitely", "You may rely on it"]
                
                
                embed = discord.Embed(title="The answer is...", colour = 0xffa500)
                
                embed.add_field(name="Answer:", value=f"{random.choice(r_answers)}")
                
                await message.channel.send(content=None, embed=embed)
            
                        
                #'''        
                #if message.content.split()[1] == "give":
                 #   if str(message.author.top_role) in settings["opRanks"]:
              #       if len(message.content.split()) == 2:
                #         user = random.choice(message.guild.members)
                    #        await message.channel.send(user.mention)
                        
                    #else:
                    #    embed = discord.Embed(title="Permission Error")
                    #    embed.add_field(name="Error", value="You do not have the permision to do this!") 
              #       await message.channel.send(content=None, embed = embed)
            #'' '
                
            elif message.content.split()[1] == "users":
                embed = discord.Embed(title="Number of users", colour = 0xffa500)
                embed.add_field(name="Amount of users:", value=message.guild.member_count) 
                await message.channel.send(content=None, embed = embed)
                    
                
            elif message.content.split()[1] == "work":
                await message.channel.send("This work")
            
                
            
            elif message.content.split()[1] == "rnum":
                messag = message.content.split()
                try:
                    minNum = int(messag[2])
                    maxNum = int(messag[4])
                    response = random.randint(minNum,maxNum)
                    await message.channel.send(response)
                except:
                    embed = discord.Embed(title="How to use rnum", colour = 0xffa500)
                    embed.add_field(name="How to use rnum", value="Here is the format: k, rnum minimumNumber - maximumNumber. E.g k, rnum 1 - 10  (PAY ATTENTION TO SPACES)") 
                    await message.channel.send(content=None, embed = embed)
                    
                    
            elif message.content.split()[1] == "ping":
                if str(message.author.top_role) in settings["opRanks"]:
                    await message.delete(delay=None)
                    
                else:
                    embed = discord.Embed(title="Permission Error", colour = 0xff0000)
                    embed.add_field(name="Error", value="You do not have the permision to do this!") 
                    await message.channel.send(content=None, embed = embed)
                

             
                    
            
client.run(TOKEN)