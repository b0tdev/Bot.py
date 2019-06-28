from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="!", status=discord.Status.idle, activity=discord.Game(name="Booting.."))

bot.remove_command("help")

@bot.event
async def on_ready():
    print(("Ready to go!"))
    print((f"Serving: {len(bot.guilds)} guilds."))
    print('Logged In Successfully')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Active!"))

@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    await ctx.channel.send(f"My ping is {ping}ms")

@bot.command()
async def user(ctx, member:discord.User = None):
    if member == None:
        member = ctx.message.author
        pronoun = "Your"
    else:
        pronoun = "Their"
    name = f"{member.name}#{member.discriminator}"
    status = member.status
    joined = member.joined_at
    role = member.top_role
    await ctx.channel.send(f"{pronoun} name is {name}. {pronoun} status is {status}. They joined at {joined}. {pronoun} rank is {role}.")

@bot.command()
async def ban(ctx, member:discord.User = None, reason = None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself!")
        return
    if reason == None:
        reason = "No reason at all!"
    message = f"You have been banned from {ctx.guild.name} for {reason}!"
    await member.send(message)
    await ctx.guild.ban(member)
    await ctx.channel.send(f"{member} is banned!")
  
   

bot.run("process.env.token")
