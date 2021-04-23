import discord
from discord.ext import commands
import asyncio


class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, * , reason = None):
        """|| Kicks a player (owner only)"""
        await member.send(f"you were kicked by {ctx.author.mention} for following resons(s) : {reason}")
        await member.kick(reason = reason)
        await ctx.send(f"{member.mention} was kick by {ctx.author.mention} reason : {reason}")
    
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, * , reason = None):
        """"|| Bans a member"""
        await member.send(f"you were baned by {ctx.author.mention} for following reason(s) : {reason} \n If you think you were banned wrongly ot would like to appeal then please join this server; \n https://discord.gg/hvuKh3GPwS")
        await member.ban(reason = reason)
        await ctx.send(f"{member.mention} was baned by {ctx.author.mention} reason : {reason}")
    
    @commands.command()
    @commands.has_guild_permissions(ban_members = True)
    async def unban(self,ctx, *, member):
        """|| Unban command no need of mention use like Expressingames#2342"""
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

        
    @commands.command()
    @commands.has_guild_permissions(manage_messages= True)
    async def clear(self,ctx, amount=0):
        """
       || Deletes messages
        """
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages = True)
    async def announce2(self,ctx, chan: discord.TextChannel, * , announcement=None):
        """|| announces something """
        if not announcement:
            await ctx.send("provide a announcement")
        await chan.send(f'{announcement}')

    @commands.command()
    @commands.has_guild_permissions(manage_messages= True)
    async def say(self,ctx, * , Text):
        await ctx.message.delete()
        await ctx.send(f"{Text}")

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages = True)
    async def dm(self,ctx, member: discord.Member, * , text=None):
        await member.send(f"{text}")
        await ctx.send(f"{member} was sent a DM by {ctx.author} Message :``` {text} ```")
        
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages = True)
    async def accept(self,ctx, member: discord.Member, * , text=None):
        await member.send(f"__**Application Result**__ \n \n Dear {member.mention}, \n Congratulations your application to become a member of staff at Scotland™ has been accepted, you will go through the next two phases shortly and will be contacted by this bot again regarding this. \n \n **Application Reader:** {ctx.author.mention} \n **Comments:** {text} \n \n Once again congratulations. \n \n Many Thanks \n {ctx.author.mention} on behalf of Scotland:tm: Management Team")
        await ctx.send(f"{member} was sent there application result which was a pass by {ctx.author} Comments :``` {text} ```")
        
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages = True)
    async def decline(self,ctx, member: discord.Member, * , text=None):
        await member.send(f"__**Application Result**__ \n \n Dear {member.mention}, \n Unfortunately your application to become a member of staff at Scotland™ has been declined. \n \n **Application Reader:** {ctx.author.mention} \n **Comments:** {text} \n \n Regards \n {ctx.author.mention} on behalf of Scotland:tm: Management Team")
        await ctx.send(f"{member} was sent there application result which was a decline by {ctx.author} Comments :``` {text} ```")


    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages = True)
    async def phase2(self,ctx, member: discord.Member):
        await member.send(f"__**Application Phase 2**__ \n \n Dear {member.mention}, \n Congratulations on your application to become a member of staff at Scotland™ being accepted, this is a DM to provide you with phase 2. \n \n **Link:** https://forms.gle/rtYm4yiWryYTcbGe7 \n \n Once again congratulations. \n \n Many Thanks \n {ctx.author.mention} on behalf of Scotland:tm: Management Team")
        await ctx.send(f"{member} was sent phase 2 by {ctx.author}")
    
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages = True)
    async def announce(self,ctx, chan: discord.TextChannel, * , announcement=None):
        """|| announces something """
        if not announcement:
            await ctx.send("provide a announcement")
        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.add_field(name="Announcement" , value=announcement)
        embed.set_footer(text=f"Sent by {ctx.author}")
        await chan.send(embed=embed)
    
   
   
def setup(bot):
    bot.add_cog(Cog(bot))
