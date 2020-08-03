import discord
from discord.ext import commands
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
  return("bot started successfully")

@client.command()
@commands.has_any_role("admins")
async def kick (ctx, member:discord.User=None, reason =None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot kick yourself")
        return
    if reason == None:
        reason = "No reason given"
    message = f"You have been kicked from {ctx.guild.name} for {reason} by"
    await member.send(message)
    # await ctx.guild.kick(member, reason=reason)
    await ctx.channel.send(f"{member} has been kicked for {reason}!")

client.run('NzM5NzczMzcwODM2NzEzNTAz.XyfVow.u8ikvxnmTRoQgGpkCzvcgFmH_rs')