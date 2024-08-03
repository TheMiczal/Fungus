#TOKEN
token = "token" #ENTER TOKEN HERE
#CHANNEL
main_channel = 1234567890 #ENTER MAIN CHANNEL HERE

#IMPORTS
import discord
import random
import datetime
from datetime import date, timezone
from logging import exception
import requests
import re
import asyncio

import pandas as pd

from discord.ext import tasks
from discord.ext.tasks import *

#MAIN VARS
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

fungus = " <:fungus:1269303722236838010>" #Main emote of Fungus

#MISC VARS
curr = "eur"
quantity = 1
result = "pln"
stats_text = ""

#PRINT
anwsers = [
    "Yes",
    "No",
    "Maybe",
    "Sometimes",
    "I don't know",
    "Try again",
    "Nah",
    "Ye",
    "idk",
    "Go away",
    fungus,
]

greetings = [
    "Heyo!" + fungus,
    "Yo!" + fungus,
    "What's up?" + fungus,
    fungus,
    "Wanna hear about my spores?" + fungus,
    "Fungi is crown of evolution!" + fungus,
    "`*ejecting spores*`",
    "Omnihostompa ended on Fungi, animalia gtfo" + fungus,
]

help = [
    "`>fungus whether X - Fungus will tell you if its good idea`",
    "`>fungus X or Y or ... - Fungus will choose`",
    "`>fungus wait X sec/min/hours text - Fungus will ping you after the time entered`",
    "`>fungus comment on X - Fungus will generate random sentence`",
    "`>fungus shitpost - Fungus will generate shitpost`",
    "`>fungus tarot X - Fungus will draw 1-6 cards`",
    "`>fungus exchange Xeur to usd - Fungus will show you current money rate. Note: Fungus uses polish api, so it converts to PLN by default.`",
    "`>fungus stats - Fungus will roll stats for your DnD character`"
]

class Quotes:
    quotes1 = []
    quotes2 = []
    quotes3 = []
    quotes4 = []
    quotes5 = []
    quotes6 = []
def load_file_to_attribute(instance, attribute_name, file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]
        setattr(instance, attribute_name, lines)
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
text_instance = Quotes()
attributes_files = {
    'quotes1': 'quotes/quotes1.txt',
    'quotes2': 'quotes/quotes2.txt',
    'quotes3': 'quotes/quotes3.txt',
    'quotes4': 'quotes/quotes4.txt',
    'quotes5': 'quotes/quotes5.txt',
    'quotes6': 'quotes/quotes6.txt',
}
for attribute, file_name in attributes_files.items():
    load_file_to_attribute(text_instance, attribute, file_name)

@client.event
async def on_message(message):
    global greetings
    global anwsers
    global help
    global quotes1
    global quotes2
    global quotes3
    global quotes4
    global quotes5
    global quotes6

    if message.author == client.user:
        return

    if message.content == "ping":
        await message.channel.send("pong")


    if message.content.startswith("fungus") or message.content.startswith("Fungus"):
        if "or" in message.content or "whether" in message.content:
            if "wait" in message.content:
                await timerr(message.content, message.author, message.channel, message.guild.id)
            elif "comment on" in message.content:
                pass
            else:
                await message.channel.send(orr(message.content))
        else:
            if "wait" in message.content:
                await timerr(message.content, message.author, message.channel, message.guild.id)
    
        if "comment on" in message.content:
            await message.channel.send(commenton())
        
        elif "help" in message.content:
            help_text = ""
            for i in range(0, len(help)):
                help_text += help[i] + "\n"
            await message.channel.send(help_text)

        elif "shitpost" in message.content:
            await message.channel.send(str(shitpost()) + fungus)
        
        elif "exchange" in message.content:
            await message.channel.send(exchange(message.content))

        elif "stats" in message.content:
            global stats_text
            stats_text = ""
            stats()
            await message.channel.send(stats_text)

        elif "tarot" in message.content:
            words = message.content.split()
            nmb = len(words)
            if nmb != 3:
                await message.channel.send(tarot(6, message.guild.id))
            else:
                try:
                    if isinstance(int(words[2]), int) == True:
                        if int(words[2]) > 0 and int(words[2]) < 7:
                            await message.channel.send(tarot(int(words[2]), message.guild.id))
                        else:
                            await message.channel.send("ERROR: Too many cards")
                except:
                    await message.channel.send("ERROR") 
        

        elif "-" in message.content or "+" in message.content or "*" in message.content or "/" in message.content or "d1" or "d2" or "d3" or "d4" or "d5" or "d6" or "d7" or "d8" or "d9" in message.content:
            text = message.content
            splitt = text.split()
            splitt.pop(0)
            text = "".join(splitt)
            split = re.split('(\d+[d]\d+)|([d]\d+)|([+])|([*])|([/])|(\W)', text)
            if None in split:
                split = list(filter(lambda item: item is not None, split))
            if '' in split:
                split = list(filter(lambda item: item is not '', split))

            rolls_total = []
            total_total = []
            rolls_num = 0

            rolls = ""
            total = 0

            for i in range(0, len(split)):
                if "d" in split[i]:
                    rolls_num+=1
                    split2 = split[i].split("d")
                    if split2[0] == "":
                        split2[0] = 1

                    for j in range(0, int(split2[0])):
                        roll = random.randint(1, int(split2[1]))
                        rolls += str(roll) + ", "
                        total += roll
                    rolls = rolls[:-1]
                    rolls = rolls[:-1]
                    split[i] = int(total)
                    rolls_total.append(rolls)
                    total_total.append(total)
                    total = 0
                    rolls = ""

            if not "r" in split and not "m" in split and not "f" in split and not "t" in split and not "s" in split and not "e" in split and not "o" in split and not "o" in split and not "x" in split:
                try:
                    for i in range(0, len(split)):
                        split[i] = str(split[i])
                    text2 = str(''.join(split))
                    score = str(eval(str(text2)))
                    if rolls_num == 0:
                        await message.channel.send("`" + str(score) + "`")
                    else:
                        score_text = ("## **Total:** `" + str(score) + "`")
                        for j in range(0, rolls_num):
                            score_text += ("\n**Roll:** `" + str(total_total[j]) + "` **→** `" + str(rolls_total[j]) + "`")
                        await message.channel.send(str(score_text))
                        rolls_num = 0
                except ZeroDivisionError:
                    await message.channel.send("https://www.youtube.com/watch?v=GPBEGV7OBbs")

def commenton():
    phrase = []
    phrase2 = ""
    for i in range(14, 14+random.randint(8, 16)):
        word = random.choice(list(open('words/words.txt')))
        phrase.append(word)
    for i in range(0, len(phrase)-1):
        phrase2 += phrase[i]
        phrase2 += " "
    phrase2 = str(''.join(phrase2.splitlines()))
    return(phrase2)

def orr(msg):
    words = msg.split()
    num_or = 0
    for i in range(0, len(words)):
        if words[i] == "or" or words[i] == "Or" or words[1] == "whether" or words[1] == "Whether":
            num_or += 1
    if words[1] == "or" or words[1] == "Or" or words[1] == "whether" or words[1] == "Whether":
        num_or = 1
    else:
        num_or = 2
    if num_or <= 1:
        random.shuffle(anwsers)
        return(anwsers[0])
    else:
        text = msg
        split = text.split()
        newsplit = []
        word = ""
        for i in range(1, len(split)):
            if split[i] == "or":
                newsplit.append(word)
                word = ""
            else:
                word += split[i] + " "
            if i == len(split)-1:
                newsplit.append(word)
        random.shuffle(newsplit)
        return(newsplit[0])

def shitpost():
    random.shuffle(text_instance.quotes1)
    random.shuffle(text_instance.quotes2)
    random.shuffle(text_instance.quotes3)
    random.shuffle(text_instance.quotes4)
    random.shuffle(text_instance.quotes5)
    random.shuffle(text_instance.quotes6)
    my_quote = ""
    my_quote += str(text_instance.quotes1[0]) + " "
    my_quote += str(text_instance.quotes2[0]) + " "
    my_quote += str(text_instance.quotes3[0]) + " "
    my_quote += str(text_instance.quotes4[0]) + " "
    my_quote += str(text_instance.quotes5[0]) + " "
    my_quote += str(text_instance.quotes6[0]) + " "
    return my_quote

def exchange(msg):
  global curr
  global quantity
  global result

  tekst = msg
  spl = tekst.split()
  if len(spl) > 2:
      curr = spl[2]
      if len(spl) >= 5:
          result = str(spl[4])
      else:
          result = "PLN"
      cfd = re.split('(\d+)', curr)
      if cfd[0] == "":
          quantity = cfd[1]
          curr = cfd[2]
      else:
          quantity = 1
          curr = cfd[0]
  
  curr = curr.upper()
  result = result.upper()
  
  if curr == result:
    return("1" + fungus)
  else:
    return(calc_curr())

def calc_curr():
    if result == "PLN":
        try:
            outcome = 0
            response = requests.get("http://api.nbp.pl/api/exchangerates/rates/c/" + str(curr) + "/?format=json")
            outcome = round(eval(str(response.json()["rates"][0]["ask"]) + "*" + str(quantity)), 2)
            return("`" + str(quantity) + " " + str(curr.upper()) + " = " + str(outcome) + " PLN" "`")
        except Exception:
            return(fungus)
    else:
        if curr == "PLN":
            try:
                buf = 0
                buf = requests.get("http://api.nbp.pl/api/exchangerates/rates/c/" + str(result) + "/?format=json")
                return("`" + str(quantity) + " " + str(curr.upper()) + " = " + str(round(eval(str(quantity) + "/" + str(buf.json()["rates"][0]["ask"])), 2)) + " " + str(result.upper()) + "`")
            except Exception:
                return(fungus)
        else:
            try:
                first = requests.get("http://api.nbp.pl/api/exchangerates/rates/c/" + str(curr) + "/?format=json")
                f = round(first.json()["rates"][0]["ask"], 2)
                second = requests.get("http://api.nbp.pl/api/exchangerates/rates/c/" + str(result) + "/?format=json")
                s = round(second.json()["rates"][0]["ask"], 2)
                
                i = int(quantity)
                if i > 0:
                    return("`" + str(i) + " " + str(curr.upper()) + " = " + str(round(eval(str(eval(str(f) + "*" + str(quantity))) + "/" + str(s)), 2)) + " " + str(result.upper()) + "`")
                else:
                    return("Not possible" + fungus)
            except Exception:
                print("trzy")
                return(fungus)

def stats():
    score = 0
    stats_total = ""
    for k in range(0, 6):
        rolls = []
        lowest = 0
        total = 0
        for i in range(0, 4):
            rolls.append(random.randint(1, 6))
            lowest = rolls.index(min(rolls))
        
        r2 = rolls.copy()
        r2.pop(lowest)
        for j in range(0, len(r2)):
            total += r2[j]
        score += total
        
        for i in range(0, len(rolls)):
            if i == lowest:
                rolls[i] = "~~" + str(rolls[i]) + "~~"
            else:
                rolls[i] = str(rolls[i])
        
        word = ""
        for i in range(0, len(rolls)):
            word += rolls[i] + ", "
        word = word[:-1]
        word = word[:-1]
        
        
        stats_total += ("[" + str(word) + "]" + " = `" + str(total) + "`\n")
  
    text = (str(stats_total) + "Total: `" + str(score) + "`")
    if score <= 75:
        stats()
    else:
        global stats_text
        stats_text = str(text)

def tarot(nmb=6, guild_id = 0):
    tarot = [
        ["The Fool", 1],
        ["The Magican", 1],
        ["The High Priestess", -2],
        ["The Empress", -1],
        ["The Emperor", 0],
        ["The Hierophant", -1],
        ["The Lovers", 1],
        ["The Chariot", 1],
        ["Strength", 2],
        ["The Hermit", 0],
        ["Wheel of Fortune", -2],
        ["Justice", 1],
        ["The Hanged Man", -6],
        ["Death", -3],
        ["Temperance", 1],
        ["The Devil", -1],
        ["The Tower", 1],
        ["The Star", 1],
        ["The Moon", 0],
        ["The Sun", 0],
        ["Judgement", 1],
        ["The World", 2],
    ]
    tarot2 = tarot
    my_cards = []
    value = 0
    list = ""
    for i in range(0, nmb):
        rng = random.randint(0, len(tarot2)-1)
        card = tarot2[rng][0]
        my_cards.append(card)
        value += tarot2[rng][1]
        tarot2.pop(rng)
        list += card
        if i < nmb-1:
            list += ", "
    
    text = ""
    if value < 0:
        t = [
            "Not good..." + fungus,
            "LOL!" + fungus,
            "Better look for coffin to buy..." + fungus,
        ]
        text = t[random.randint(0, len(t)-1)]
    elif value > 0:
        t =[]
        t = [
            "LOL! " + fungus,
            "Noice " + fungus,
            "Looks Good " + fungus,
        ]
        text = t[random.randint(0, len(t)-1)]
    elif value == 0:
        text = fungus
    output = "Cards: `" + str(list) + "`\n" + str(text)
    return output

async def timerr(text, author, channel, id):
    channel1 = channel
    guild_id = id

    spl = text.split()
    if len(spl) < 4:
        await channel1.send("ERROR!")
        return
    quantity = spl[2]
    unit = spl[3].lower()
    reason = "Ping!"
    if len(spl) > 4:
        spl2 = spl
        del spl2[0]
        del spl2[0]
        del spl2[0]
        del spl2[0]
        reason = " ".join(spl2)
    
    time = 0
    if "s" in unit:
        time = int(quantity)
    elif "m" in unit:
        time = int(quantity) * 60
    elif "h" in unit:
        time = int(quantity) * 60 * 60
    else:
        await channel1.send(author.mention + " error!")
        return

    call(time, unit, reason, author, channel, guild_id)


async def task(time, unit, reason, author, channel, guild_id):
    channel1 = channel
    anwser = [
        "kk",
        "Okay",
        "Ay ay",
        "Timer started!"
    ]
    random.shuffle(anwser)
    await channel1.send(anwser[0])
    await asyncio.sleep(float(time))
    await channel1.send(author.mention + " " + str(reason))

def call(time = 1, unit = "sec", reason = "", author = "", channel = main_channel, guild_id = 0):
    t = asyncio.create_task(task(time, unit, reason, author, channel, guild_id))

def hello():
    rng = random.randint(1, 8)
    if rng == 1:
        r = shitpost()
        return r
    else:
        global greetings
        random.shuffle(greetings)
        return greetings[0]

@tasks.loop(hours=4)
async def send_hello():
    channel1 = client.get_channel(int(main_channel))
    await channel1.send(hello())

@client.event
async def on_ready():
    print('Logged as {0.user}'.format(client))
    send_hello()
    send_hello.start()

client.run(token)