import discord
import os
import t1
token = "MTAxMDI0NTM0MjY5Mzk1NzY1Mw.GntHra.xzgtOwTjuTRMw58xSUq6plfN3rsJSoOX9E6Xcg"
ls=["Students",]
key="meow"
client = discord.Client(intents=discord.Intents.default())
@client.event
async def on_ready():print(f"MODOC logged in as {client.user}")
@client.event
async def on_message(message): 
  if message.author != client.user :
    if key in message.content:
      print(message.author.nick[0:10])
      ls.append(message.author.nick[0:10])
      print(ls)  
  with open('students.csv', 'w') as fp:
    for item in ls:
      fp.write("%s\n" % item)
  if message.content.startswith('!send'):
    t1.func()
    '''fu1=open("students.csv","w")
    fu1.write(ls[0])
    fu1.close()'''
  await message.delete()
client.run(token)
