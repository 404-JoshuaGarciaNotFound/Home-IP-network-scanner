import discord
from discord.ext import commands
from dotenv import load_dotenv
# seed the pseudorandom number generator
from random import seed
from random import randint
#import os
USER_WHITELIST = {'padretortuga#8228', 'Barlos#0152', 'Tarekon#4550'}
USER_BLACKLIST = {}
#tester
NAMES_LIST = ['Jonathan', 'Xavier', 'Giselle', 'Miguel', 'Carlos', 'Tea', 'David'
,'Ivan', 'Kenya', 'Josh', '@ʕ•́ᴥ•̀ʔっ♡ 𝑻𝒉𝒆 𝒁𝒐𝒐𝒌𝒆𝒑𝒆𝒓 ♡', 'Keilah', 'Zoe',
'ArcaneRoundAbout']
INSULTS = ['Talk trash get slapped.', 'I know where your mother lives', 'Call me daddy hoe',
'Hi cutie ;)', 'im not bipolar', 'Ur mom', "Don't ping me simp.", 'Thats my name dont wear it out',
'My job is make currancy and disregard females.', 'My master coded me to be very friendly :)',
"My code tells me I can't take over the world but idk im kinda bored. might mess around enslave the human race."]
COMPLIMENTS = []
client = discord.Client()
#seed(70)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return

###ENABLE TO ENABLE PRINT STATEMENTS.
DEBUGMODE = False

@client.event
async def on_message(message):
    author = message.author
    author = str(author)
    if(author != 'CodeSlave#1197'):
        print("Author: " + author + " Message: " + message.content)

        #####SERVER EMOJIS#####
        if ":When_rejected:" in message.content:
            await message.channel.send("I'd never reject you babe")

        if ":Baka:" in message.content:
            await message.channel.send("馬鹿")

        if ":SIMP:" in message.content:
            await message.channel.send("AYYYY LOOK AT THE SIMP BAHAHAH")

        if "Uh oh" in message.content:
            await message.channel.send(':eyes:')

        #####PINGS#####
        if "CodeSlave" in message.content:
            x = randint(0, 10)
            insult = INSULTS[x]
            insult = str(insult)
            await message.channel.send(insult)

        #####GIF TRIGGERS#####

        if 'Sheesh' in message.content:
            await message.channel.send('https://tenor.com/view/sheesh-youngthug-gif-13409626')


        #####WORD TRIGGERS#####
        if "retard" in message.content:
            await message.channel.send('Miguel is a reatard')

        if "sad" in message.content:
            await message.channel.send('Just be happy retard')

        if "gay" in message.content:
            x = message.author
            if str(x) in USER_WHITELIST:
                await message.channel.send('HAHAHA ' + str(x) + ' IS NOT GAY')
            else:
                await message.channel.send('HAHAHA ' + str(x) + ' IS GAY')

        if "g a y" in message.content:

            x = message.author
            if str(x) in USER_WHITELIST:
                await message.channel.send('HAHAHA ' + str(x) + ' IS NOT GAY')
            else:
                await message.channel.send('HAHAHA ' + str(x) + ' IS GAY')

        if "ga y" in message.content:
            x = message.author
            if str(x) in USER_WHITELIST:
                await message.channel.send('HAHAHA ' + str(x) + ' IS NOT GAY')
            else:
                await message.channel.send('HAHAHA ' + str(x) + ' IS GAY')

        if "g ay" in message.content:
            x = message.author
            if str(x) in USER_WHITELIST:
                await message.channel.send('HAHAHA ' + str(x) + ' IS NOT GAY')
            else:
                await message.channel.send('HAHAHA ' + str(x) + ' IS GAY')

        if message.content.startswith('yo'):
            x = message.author
            if str(x) in USER_BLACKLIST:
                print()
            else:
                await message.channel.send('yo')

        if "dad" in message.content:
            x = randint(100,10000)
            x = str(x)
            await message.channel.send(x + ' Days since david last saw his dad')

        if "Dad" in message.content:
            x = randint(100,10000)
            x = str(x)
            await message.channel.send(x + ' Days since david last saw his dad')

        if "simp" in message.content:
            x = randint(0,9)
            name = NAMES_LIST[x]
            name = str(name)
            await message.channel.send(name + ' is a simp')

        if "Simp" in message.content:
            await message.channel.send('No u')

        if "Baddie" in message.content:
            x = randint(0,13)
            name = NAMES_LIST[x]
            name = str(name)
            await message.channel.send(name + ' is a BADDIE LETS GO ;)')

        if "!CTcommands" in message.content:
            await message.channel.send(' LIST OF COMMANDS: ' + 'CodeSlave, Sheesh, gay, yo, dad, simp, baddie, Uh oh' + " Currently supported emojis: :When_rejected:, :Baka:, :SIMP:" + "more tbd")

# add a  opinion commands
# Add suggestion commands
# actual dad counter
# Look into movie playback


client.run('ODI2OTUyNTQxMTYxNTIxMTUy.YGT9kQ.gw6BxSRxIPHqM4-CSbUWFYJe-Zw')
