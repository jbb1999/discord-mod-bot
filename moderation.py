import discord
from discord.ext import commands
import random
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot online')

#Kick
@client.command()
@commands.has_any_role("admins") # Selects which roles are able to use the command
async def kick (ctx, member:discord.User=None, *, reason =None):
    if member == None or member == ctx.message.author: # Makes kicking yourself impossible and if no reason is given it will set default to For being a jerk(line 17).
        await ctx.channel.send("You cannot kick yourself")
        return
    if reason == None:
        reason = "For being a jerk!"
    message = f"You have been kicked from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.kick(member, reason=reason) #kicks the user
    await ctx.channel.send(f"{member} has been kicked! {reason}") #send message to kicked user

#Ban
@client.command()
@commands.has_any_role("admins")# makes command only usable by admins
async def ban (ctx, member:discord.User=None, *, reason =None):
        if member == None or member == ctx.message.author: # Makes banning yourself impossible and if no reason is given it will set default to For being a jerk(line 31).
            await ctx.channel.send("You cannot ban yourself??? I should really question your admin.....")
            return
        if reason == None:
            reason = "For being a jerk!"
        message = f"You have been banned from {ctx.guild.name} {reason}"
        await member.send(message)
        await ctx.guild.ban(member, reason=reason, delete_message_days=0) #bans the user and delets no messages
        await ctx.channel.send(f"{member} has been banned from {ctx.guild.name} for {reason}") #send message in chat
#unban
@client.command()
@commands.has_any_role("admins")# makes command only usable by admins
async def unban (ctx, member:discord.User=None, *, reason =None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot unban yourself??? I should really question your admin.....")
            return
        if reason == None:
            reason = "being on my good side!"
        message = f"You have been unbanned from {ctx.guild.name} for {reason}"
        await member.send(message)
        await ctx.guild.unban(member, reason=reason,) #unbans the user
        await ctx.channel.send(f"{member} has been unbanned from {ctx.guild.name} for {reason}") #send message to chat

client.run('')