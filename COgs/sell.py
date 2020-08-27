import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.cooldowns import BucketType

class marketplace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1,3600,BucketType.member)
    async def sell(self, ctx):
        await ctx.send('Look for a DM by <@681537574593888336>')
        await ctx.author.send("What product is being sold?")
        def check(msg):
            return not msg.guild and msg.author == ctx.author
        try:
            item = await self.bot.wait_for('message', check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.author.send("Timed out")
        else:
            await ctx.author.send("How much are you selling this for?")
            try:
                price = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.author.send("Timed out")
            else:
                await ctx.author.send("What features does this product have?")
                try:
                    note = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("Timed out")
                else:
                    await ctx.author.send("Please provide an image, not a link.")
                    try:
                        Image = await self.bot.wait_for('message', check=check, timeout=120)
                        attachment = Image.attachments[0]
                        attachment_url = attachment.url
                    except asyncio.TimeoutError:
                        await ctx.author.send("Timed out")
                    else:
                        await ctx.author.send("Your advert has been published! Look in <#724241250764455957>")

        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name="Product Advertisement")
        embed.add_field(name="Product:", value=f"{item.content}", inline=False)
        embed.add_field(name="sold by:", value=f"{ctx.author.mention}", inline=False)
        embed.add_field(name="Price:", value=f"{price.content}", inline=False)
        embed.add_field(name="Features:", value=f"{note.content}", inline=False)
        embed.set_image(url=attachment_url)
        channel = self.bot.get_channel(724241250764455957)
        await channel.send(embed=embed)

    @commands.command()
    @commands.cooldown(1,3600,BucketType.member)
    async def hire(self, ctx):
        await ctx.send('check your dm')
        await ctx.author.send("Whom are you hiring?")
        def check(msg):
            return not msg.guild and msg.author == ctx.author
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
        channel = self.bot.get_channel(724241277826105374)
        await channel.send(embed=embed)



    @commands.command()
    @commands.cooldown(1,3600,BucketType.member)
    async def ad(self, ctx):
        await ctx.send('check your dm')
        await ctx.author.send("Whats the name of your company")
        def check(msg):
            return not msg.guild and msg.author == ctx.author
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
        embed.add_field(name="Description", value=notes.content)
        embed.add_field(name="link" , value =f"{price.content}")
        embed.set_image(url=attachment_url)
        embed.set_footer(text=f"Send by {ctx.author}")
        channel = self.bot.get_channel(724241221395939330)
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
