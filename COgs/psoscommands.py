import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.cooldowns import BucketType

class psoscommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role(771443177688793131, 771442588435349554, 771444351284019220)
    async def psostraining(self, ctx):
        await ctx.reply(content="**Please check your DMs!**")
        embed1 = discord.Embed(title="Time", description="When will the training start? UK time only please.")
        await ctx.author.send(embed=embed1)
        def check(msg):
            return not msg.guild and msg.author == ctx.author
        try:
            time = await self.bot.wait_for('message', check=check, timeout=120)
        except asyncio.TimeoutError:
            await ctx.author.send("Timed out")
        else:
            embed2 = discord.Embed(title="Help", description="Who will help in the traing, provie there roblox username. If no one just say **NO ONE**")
            await ctx.author.send(embed=embed2)
            try:
                help = await self.bot.wait_for('message', check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.author.send("Timed out")
            else:
                embed3 = discord.Embed(title="Time", description="When should the trainees join for? UK time only please.")
                await ctx.author.send(embed=embed3)
                try:
                    time2 = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("time out!")
                else:
                  embed4 = discord.Embed(title="Invite", description="Please provide an invite for <#834439462334758964>")
                await ctx.author.send(embed=embed4)
                try:
                    link = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("time out!")
                else:
                  embed5 = discord.Embed(title="Rank", description="What rank and below should attend. Provdce the ID.")
                await ctx.author.send(embed=embed5)
                try:
                    role = await self.bot.wait_for('message', check=check, timeout=120)
                except asyncio.TimeoutError:
                    await ctx.author.send("time out!")
                else:
                    await ctx.author.send(f"Your training has been posted!")
                
        title = "It's training time!"
        description = f"**{time.content}** \n\n Everyone is expected to be there from the rank of <@&{role.content}> downwards. \n\n **{help.content}** Will assist me in the training, you will all be taking part.\n\n You will join {link.content} at {time2.content}. \n\n Hosted by: {ctx.author}"
        embed = discord.Embed(title = title , description = description)
        channel = self.bot.get_channel(840172742212583444)
        await channel.send("this will be a ping after testing")
        await channel.send(embed = embed)
        
        
def setup(bot):
    bot.add_cog(psoscommands(bot))
