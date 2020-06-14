import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.cooldowns import BucketType

class marketplace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.dm_only()
    @commands.cooldown(1,3600,BucketType.member)
    async def sell(self, ctx):
        await ctx.author.send("what product are you selling?")
        def check(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
        try:
            item = await self.bot.wait_for('message', check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.author.send("Timed out")
        else:
            await ctx.send("Whats the price?")
            try:
                price = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.author.send("Timed out")
            else:
                await ctx.send("Any note?")
                try:
                    note = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("Timed out")
                else:
                    await ctx.author.send("please provide a image (no links) ")
                    try:
                        Image = await self.bot.wait_for('message', check=check, timeout=120)
                        attachment = Image.attachments[0]
                        attachment_url = attachment.url
                    except asyncio.TimeoutError:
                        await ctx.author.send("Timed out")
                    else:
                        await ctx.author.send("DONE!")

        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name="a new item")
        embed.add_field(name="Product:", value=f"{item.content}")
        embed.add_field(name="sold by:", value=f"{ctx.author}")
        embed.add_field(name="Price:", value=f"{price.content}")
        embed.add_field(name="Note:", value=f"{note.content}")
        embed.set_image(url=attachment_url)
        channel = self.bot.get_channel(681051529427550212)
        await ctx.author.send(embed=embed)
        await channel.send(embed=embed)

    @sell.error
    async def sell_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"Hey! you need to wait {(int(error.retry_after/60))} mins before using it again!")

def setup(bot):
    bot.add_cog(marketplace(bot))