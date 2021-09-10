from discord.ext import commands
from pathlib import Path
from verification.api import getcataLevel
from verification.api import disc
from discord.utils import get
import discord

def verificationrun():
    bot = commands.Bot(command_prefix='-', help_command=None)

    with open(Path('verification/token.txt'), 'r') as file:
        token = file.read()



    @bot.command()
    async def verify(ctx, arg):
        sender = ctx.author
        try:
            catalvl = getcataLevel(arg)
            d = disc(arg)
            # if str(sender) != d:
            #     await ctx.author.send("Please verify your own account and connect your discord account to hypixel in the social menu.")
            #     await ctx.message.delete()
            #     return verify
            await sender.edit(nick=f'[{catalvl}] {arg}')
            await ctx.message.delete()
            name = f'Cata {catalvl}'
            try:
                role = get(sender.guild.roles, name=name)
                await sender.add_roles(role)
            except AttributeError:
                role = await sender.guild.create_role(name=name)
                await sender.add_roles(role)                
            return verify

        except discord.Forbidden:
            await sender.send("This bot has lower permissions than you so please manually update your nickname.")
            await ctx.message.delete()
            return verify

    @bot.event
    async def on_message(message):
        await message.delete()
        await bot.process_commands(message)
        return on_message

    bot.run(token)