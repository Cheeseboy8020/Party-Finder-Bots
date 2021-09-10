import discord
from discord.ext import commands
from discord.utils import get
from pathlib import Path

def classelectorrun():
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix='-', help_command=None, intents=intents)

    with open(Path('reactionsetuprole/token.txt'), 'r') as file:
        token = file.read()

    @bot.event
    async def on_raw_reaction_add(payload):
        reactor = payload.member
        if payload.emoji.name == 'Tank':
            role = get(reactor.guild.roles, name='Tank')
            await reactor.add_roles(role)
        elif payload.emoji.name == 'Archer':
            role = get(reactor.guild.roles, name='Archer')
            await reactor.add_roles(role)
        elif payload.emoji.name == 'Berserk':
            role = get(reactor.guild.roles, name='Berserk')
            await reactor.add_roles(role)
        elif payload.emoji.name == 'Mage':
            role = get(reactor.guild.roles, name='Mage')
            await reactor.add_roles(role)
        elif payload.emoji.name == 'Healer':
            role = get(reactor.guild.roles, name='Healer')
            await reactor.add_roles(role)
        else:
            return

    @bot.event
    async def on_raw_reaction_remove(payload):
        guild = discord.utils.find(lambda g : g.id == payload.guild_id, bot.guilds)
        reactor = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        if payload.emoji.name == 'Tank':
            role = get(guild.roles, name='Tank')
            await reactor.remove_roles(role)
        elif payload.emoji.name == 'Archer':
            role = get(reactor.guild.roles, name='Archer')
            await reactor.remove_roles(role)
        elif payload.emoji.name == 'Berserk':
            role = get(reactor.guild.roles, name='Berserk')
            await reactor.remove_roles(role)
        elif payload.emoji.name == 'Mage':
            role = get(guild.roles, name='Mage')
            await reactor.remove_roles(role)
        elif payload.emoji.name == 'Healer':
            role = get(guild.roles, name='Healer')
            await reactor.remove_roles(role)
        else:
            return
    bot.run(token)