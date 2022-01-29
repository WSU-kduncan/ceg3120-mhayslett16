import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
   # members = '\n - '.join([member.name for member in guild.members])
   # print(f'Guild Members:\n - {members}')

#client.run(TOKEN)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    hitchhiker_quotes = [
        'There is an art, it says, or rather, a knack to flying. The knack lies in learning how to throw yourself at the ground and miss.',
        'It is a mistake to think you can solve any major problems just with potatoes.',
        'In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move.',
        'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.',
    ]
 
    levi_quotes = [
        'This is just my opinion, but when it comes to teaching somebody discipline…I think pain is the most effective way. ',
        'If you don’t want to die, think! ',
        'The difference between your decision and ours is experience. But you don’t have to rely on that. ',
        'Believe in yourself, or believe in the survey corps and me. I don’t know and I never have but I can believe in my own abilities or the choices of the companions I trust. But no one ever knows how it will turn out. So choose for yourself, whichever decision you will regret the least. ',
        'A lot of time, you’re going into situation you know nothing about. So what you need is to be quick to act…and make tough decisions in worst-case scenarios. ',
        'The lesson you need to learn right now can’t be taught with words, only with action. ',
        'It’s good to see that someone has the balls to go… but don’t forget to do your damnedest to stay alive. ',
        'Don’t get me wrong. It’s not like I trust him. If he betrays us or goes berserk, I’ll put him down without hesitation. ',
        'Some scouts’ lives are more valuable than others, only those dumb enough to acknowledge that join us. ',
        'Im going to kill you and ship your corpse back to Marley, with a note about your little plot. '
        ]

    if message.content == 'Levi!':
        #response = random.choice(brooklyn_99_quotes)
        #response = random.choice(hitchhiker_quotes)
        response = random.choice(levi_quotes)
        await message.channel.send(response)

client.run(TOKEN)
