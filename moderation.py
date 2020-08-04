import discord
from discord.ext import commands
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot online')

#Kick
@client.command()
@commands.has_any_role("admins")
async def kick (ctx, member:discord.User=None, *, reason =None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot kick yourself")
        return
    if reason == None:
        reason = "For being a jerk!"
    message = f"You have been kicked from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.kick(member, reason=reason)
    await ctx.channel.send(f"{member} has been kicked! for {reason}")

client.run('Token')