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
        embed.add_field(name="sold by:", value=f"{ctx.author.mention}")
        embed.add_field(name="Price:", value=f"{price.content}")
        embed.add_field(name="Note:", value=f"{note.content}")
        embed.set_image(url=attachment_url)
        channel = self.bot.get_channel(681051529427550212)
        await channel.send(embed=embed)

    @commands.command()
    @commands.dm_only()
    @commands.cooldown(1,3600,BucketType.member)
    async def hire(self, ctx):
        await ctx.author.send("Whom are you hiring?")
        def check(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
        try:
            hire = await self.bot.wait_for('message', check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.author.send("Timed out")
        else:
            await ctx.author.send("anynotes?")
            try:
                notes = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.author.send("Timed out")
            else:
                await ctx.author.send("how much are you paying")
                try:
                    price = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("time out!")
                else:
                    await ctx.author.send("done!")
                

        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name="**Hiring**")
        embed.add_field(name="Name:", value=f"{ctx.author.mention}")
        embed.add_field(name="Hiring:", value=hire.content)
        embed.add_field(name="payment:", value=price.content)
        embed.add_field(name="Notes:", value=notes.content)
        channel = self.bot.get_channel(714537321734602893)
        await channel.send(embed=embed)



    @commands.command()
    @commands.dm_only()
    @commands.cooldown(1,3600,BucketType.member)
    async def ad(self, ctx):
        await ctx.author.send("Whats the name of your company")
        def check(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
        try:
            name = await self.bot.wait_for('message', check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.author.send("Timed out")
        else:
            await ctx.author.send("please give a breif discription")
            try:
                notes = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.author.send("Timed out")
            else:
                await ctx.author.send("please provide a link")
                try:
                    price = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("time out!")
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
        embed.set_author(name=f"advertisement")
        embed.add_field(name="name", value=name.content)
        embed.add_field(name="discription", value=notes.content)
        embed.add_field(name="link" , value =f"{price.content}")
        embed.set_image(url=attachment_url)
        channel = self.bot.get_channel(681051648285474829)
        await channel.send(embed=embed)
        

    @sell.error
    async def sell_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"Hey! you need to wait {(int(error.retry_after/60))} mins before using it again!")

    @hire.error
    async def sell_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"Hey! you need to wait {(int(error.retry_after/60))} mins before using it again!")

    @ad.error
    async def sell_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"Hey! you need to wait {(int(error.retry_after/60))} mins before using it again!")

def setup(bot):
    bot.add_cog(marketplace(bot))