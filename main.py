import discord
import os
# import requests
# import json
import random
from keep_alive import keep_alive
from discord.utils import get

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

embed = discord.Embed()
embed.description = '''Nothing for now!'''

# lame_words = ["hi",  "hello",  "hey", "bye",  "how are you"]

# encourage = ["pera","Pera"]

# encourage_lite = [
#   "Chill!",
#   "Have a relax!",
#   "Kub kosto?😥",
#   "এত কষ্ট কেন তোমার?"
# ]

# reply_words = [
#  "bol",
#  "batao",
#  "ji?",
#  "কিছু বলবা ছোট্ট বন্ধু?"
# ]

# slang_reply = [
#   "Bashay ki adob kayda kisu shikhay nai? beyadob kothakar!",
#   "Polapain beshi paika gese!",
#   "Bhalo hoite poysha lage na!",
#   "Shutiye lal kore dibo, nongramo ber kore dibo!"
# ]

# slang_words = ['shit', 'SHIT', 'Shit', 'fuck', 'FUCK', 'Fuck', 'mother fucker', 'MOTHER FUCKER', 'Mother Fucker', 'bal', 'BAL', 'Bal', 'kutta', 'KUTTA', 'Kutta']
    
# for i in range(len(lame_words)):
#   lame_words.append(lame_words[i].upper())
#   lame_words.append(lame_words[i].title())

# def update_slang(new_slang):
#   global slang_words
#   slang_words.append(new_slang)
    
# def update_reply(new_reply):
#   global slang_reply
#   slang_reply.append(new_reply)

def nick_change(nameL):
  global nick
  nick.append(nameL)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_update(before,after):
  bname = before.nick
  aname = after.nick
  channel = discord.utils.get(before.guild.channels, name='verify')
  verify = client.get_channel(channel.id)
  print(bname,aname)
  if str(bname) == 'None' or str(aname) == 'None':
    if str(bname) == 'None' and str(aname) == 'None':
      pass
    elif str(aname) == "None" and 'CSE' in bname:
      await after.edit(nick=f"{bname}")
      await verify.send("Contract admin in order to change nickname! {}".format(before.mention))
  else:
    if len(aname) == 3:
      if aname != 'CSE' and 'CSE' in  bname:
        aname = bname
        await after.edit(nick=f"{aname}")
        await verify.send("Contract admin in order to change nickname! {}".format(before.mention))
      elif aname == 'CSE':
        aname = aname+'_No Name'
        await after.edit(nick=f"{aname}")
        await verify.send("Are you okay? {}".format(before.mention),file = discord.File('stop.gif'))
    elif len(aname)<4:
      if 'CSE' in bname:
        aname = bname
        await after.edit(nick=f"{aname}")
        await verify.send("Contract admin in order to change nickname! {}".format(before.mention))
    elif aname[0:3] == 'CSE' and bname[0:3] == 'CSE':
      pass
    elif bname[0:3] == 'CSE':
      aname = bname
      await after.edit(nick=f"{aname}")
      await verify.send("Contract admin in order to change nickname! {}".format(before.mention))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  
  # for i in range (len(slang_words)):
  #   if slang_words[i] in message.content:
  #     await message.reply(random.choice(slang_reply))
  
  # for i in range (len(lame_words)):
  #   if msg.startswith(lame_words[i]):
  #     await message.reply(random.choice(reply_words))

  # for i in range (len(encourage)):
  #   if encourage[i] in message.content:
  #     await message.reply(random.choice(encourage_lite))

  # if msg.startswith("$add"):
  #   new_slang = msg.split("$add ",1)[1]
  #   if new_slang not in slang_words:
  #     update_slang(new_slang.lower())
  #     update_slang(new_slang.upper())
  #     update_slang(new_slang.title())
  #     await message.reply("New slang word added.")
  #   else:
  #     await message.reply("Already added.")
  
  # if msg.startswith("$reply"):
  #   new_reply = msg.split("$reply ",1)[1]
  #   if new_reply not in slang_reply:
  #     update_reply(new_reply)
  #     await message.reply("New line added.")
  #   else:
  #     await message.reply("Already added.")

  # if msg.startswith("$list"):
  #   await message.reply(f"Slang words = {slang_words}")

  if msg.startswith("$clear"):
    if str(message.author) == "Build different#4172":
      cut = msg.split("$clear ",maxsplit=1)
      total_del = int(cut[1])+1
      await message.channel.purge(limit=total_del)
    else:
      await message.channel.purge(limit=1)
      await message.reply("You don't have permission to do that {}".format(message.mention))

  if msg.startswith("$"):
    list1 = ['cse101','cse110','cse111','clear','rules','verify']
    count = 0
    cut = msg.split("$")
    for i in cut:
      if i not in list1:
        count+=1
      else:
        count = 0
        break
    if count != 0:
      await message.channel.purge(limit=1)

  if msg.startswith("$rules"):
    if str(message.author) == "Build different#4172":
      await message.channel.purge(limit=1)
      file1 = open('rules.txt','r')
      embed.description = file1.read()
      await message.channel.send(embed=embed)
      file1.close()
    else:
      await message.channel.purge(limit=1)
  # if msg.startswith("$football vejaal"):
  #   await  message.channel.send(file = discord.File('football.jpg'))

  if msg.startswith("$verify"):
    if str(message.author) == "Build different#4172":
      await message.channel.purge(limit=1)
      file2 = open('verify.txt','r')
      embed.description = file2.read()
      await message.channel.send(embed=embed)
      file2.close()
    else:
      await message.channel.purge(limit=1)

keep_alive()
client.run(os.getenv('TOKEN'))

  # if msg.startswith("$changenick"):
  #   new_nick = nick[0]
  #   if len(nick[0]) > 4 and new_nick[0:3] != 'JaaL':
  #     await discord.Member.edit(nick="JaaL"+nick[0])
  #     await message.reply("worked1!")
  #   elif len(nick[0]) < 4:
  #     await discord.Member.edit(nick="JaaL"+nick[0])
  #     await message.reply("worked2!")
  #   else:
  #     await message.reply("Your already a family member!")