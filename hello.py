"""
python-lorem
"""
import discord
import lorem

# this is the equivalent of `discord.ext.commands`
from core import custom as commands

class MyCog(commands.Cog):
    # you don't have to define __init__
    # as the bot is already passed when
    # the cog is loaded into the bot

    @commands.command()
    async def my_command(self, ctx: commands.Context):
        stc = sentence(count=1, comma=(0, 5), word_range=(5, 20))
        await ctx.send(f"Hello Git!\n\n{stc}")
    
async def setup(bot: commands.Bot, guild_id: int):
    await bot.add_cog(MyCog(guild_id))
