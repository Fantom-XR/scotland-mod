import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.cooldowns import BucketType

class new(new.Cog):
    def __init__(self, bot):
        self.bot = bot
        @commands.command()
    @commands.cooldown(0,0000,BucketType.member)
    async def new(self, ctx):
        await ctx.send('Look for a DM by <@681537574593888336>')
        await ctx.author.send("What is the name of the free product?")
        def check(msg):
            return not msg.guild and msg.author == ctx.author
        try:
            name = await self.bot.wait_for('message', check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.author.send("Timed out")
        else:
            await ctx.author.send("Give a description of the new free product.")
            try:
                notes = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.author.send("Timed out")
            else:
                await ctx.author.send("Provide download link.")
                try:
                    price = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("time out!")
                else:
                    await ctx.author.send("Provide an imageof the free product, it can NOT be a link.")
                    try:
                        Image = await self.bot.wait_for('message', check=check, timeout=120)
                        attachment = Image.attachments[0]
                        attachment_url = attachment.url
                    except asyncio.TimeoutError:
                        await ctx.author.send("Timed out")
                    else:
                        await ctx.author.send("The new product has been published! Look in <#724268251894513674>")
                
        
        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name=f"**Free Product**")
        embed.add_field(name="Free Product ||", value=name.content, inline=False)
        embed.add_field(name=value=notes.content, inline=False)
        embed.add_field(name="Download it here!" , value =f"{price.content}", inline=False)
        embed.set_image(url=attachment_url)
        channel = self.bot.get_channel(724268251894513674)
        await channel.send(embed=embed)
        

    @new.error
    async def sell_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"❌ This command is time-locked. Please wait {(int(error.retry_after/00))} minutes before retrying.")

def setup(bot):
    bot.add_cog(new(bot))
