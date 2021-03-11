import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.cooldowns import BucketType

class marketplace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def nhs(self, ctx):
        await ctx.send('Check for a DM by <@814857112458100736>')
        await ctx.author.send("""**NHS Scotland™️ Application**

Hello, This is the Application for NHS, Take your Time, Be Honest.


Do not ask for anyone to read your Application.

Say "next" to continue, or say "cancel" if you wish not to do the application.
""")
        def check(msg):
            return not msg.guild and msg.author == ctx.author
        try:
            item = await self.bot.wait_for('message', check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.author.send("Timed out")

        if item.content == 'cancel':
            return

        else:
            await ctx.author.send("ROBLOX Username")
            try:
                name = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.author.send("Timed out")
            else:
                await ctx.author.send("Do you have experience in any kind of Medical Services on Roblox?")
                try:
                    activity = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("Timed out")
                else:
                    await ctx.author.send("Why should we choose you over other candidates?")
                    try:
                        part = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.author.send("What treatment should be provided when someone is in Cardiac Arrest?")
                        try:
                            expereince = await self.bot.wait_for('message', check=check, timeout=120)
                        except asyncio.TimeoutError:
                            await ctx.author.send("Timed out")
                        else:
                            await ctx.author.send("What would you do if you arrived to a a patient face down on the ground?")
                    try:
                        expereince1 = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.author.send("What is the duties of a Student Paramedic?")
                    try:
                        equipment = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                             await ctx.author.send("Do you understand if you fail, A reason does not have the be provided? \n Yes, No")
                    try:
                        them = await self.bot.wait_for('message', check=check, timeout=120)
                    except asyncio.TimeoutError:
                        return
                    else:
                            await ctx.author.send('Thanks for Applying \n You will be messahed shortly with the result of your application.')

        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.set_author(name=f"New Application")
        embed.add_field(name="ROBLOX Username", value=name.content, inline=False)
        embed.add_field(name="Do you have experience in any kind of Medical Services on Roblox?", value=activity.content, inline=False)
        embed.add_field(name="Why should we choose you over other candidates?", value=part.content, inline=False)
        embed.add_field(name="What treatment should be provided when someone is in Cardiac Arrest?", value=expereince.content, inline=False)
        embed.add_field(name="What would you do if you arrived to a a patient face down on the ground?", value=expereince1.content, inline=False)
        embed.add_field(name="What is the duties of a Student Paramedic?", value=equipment.content, inline=False)
        embed.add_field(name="Do you understand if you fail, A reason does not have the be provided?", value=them.content, inline=False)
        embed.set_footer(text=f"Sent by {ctx.author} | User ID: {ctx.author.id}")
        channel = self.bot.get_channel(818090547276939264)
        msg = await channel.send(embed =embed)
    await msg.add_reaction("🟢")
    await msg.add_reaction("🟡")
    await msg.add_reaction("🔴")

  

def setup(bot):
    bot.add_cog(marketplace(bot))
