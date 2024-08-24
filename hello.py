"""
python-lorem
"""
import discord
import lorem
from functools import partial

# this is the equivalent of `discord.ext.commands`
from core import custom as commands

class MyCog(commands.Cog):
    # you don't have to define __init__
    # as the bot is already passed when
    # the cog is loaded into the bot

    @commands.command()
    async def my_command(self, ctx: commands.Context):
        stc = await self.bot.loop.run_in_executor(
            None, 
            partial(lorem.get_sentence, count=1, comma=(0, 10), word_range=(5, 20))
        )
        await ctx.send(f"Hello Git!\n\n{stc}")

async def setup(bot: commands.Bot, guild_id: int=None):
    await bot.add_cog(MyCog(guild_id))
