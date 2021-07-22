import keep_alive
import discord
import json
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
token=os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?', description='ok', intents=intents)



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name="Happy Birthday Shriannshi 🎉 !!"))


@bot.event
async def on_message(message):
    f = open('answers.json',)
    data = json.load(f)

    user = message.author
    channel=message.channel
    ch=str(channel)
    index=''.join(char for char in ch if char.isdigit())    
    try:
        obj=data['questions'][int(index)]
        if obj['channel']==ch and message.content.lower()==obj['answer']:
            roleplus = user.guild.get_role(int(obj['roleadd']))
            await user.add_roles(roleplus)
            roleminus=user.guild.get_role(int(obj['rolerem']))
            await user.remove_roles(roleminus)
            f.close()
    except:
        pass
    
#server start
keep_alive.keep_alive()
#login    
bot.run(token,bot=True,reconnect=True)