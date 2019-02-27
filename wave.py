##############################################################################################################################
# ℹ️ | S T A R T U P
##############################################################################################################################

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import json
import datetime
from datetime import datetime
import time
import bs4, requests
import os

bot = commands.Bot(command_prefix=';')
msglimit = 100
now = datetime.now()
ver = "0.0.0"
botname = "WΛVE"
temprule = "Undefined"

#Emoji
wave = "https://cdn.discordapp.com/attachments/535747082192027651/543664215773282305/sq_wave.png"
warning = "https://cdn.discordapp.com/attachments/499771950764261396/515272525626867722/warning.png"
dis_cord = "https://cdn.discordapp.com/attachments/499771950764261396/500485578794729482/discord_logo1600.png"

@bot.event
async def on_ready():
	servers = list(bot.servers)
#status = f"over {str(len(bot.servers))} servers"
	status = f"over the server"
	print ("------------------------------------")
	print (f"Bot Name: {bot.user.name}")
	print (f"Bot ID: {bot.user.id}")
	print (f"Discord Version: {discord.__version__}")
	print (f"Bot is up and running...")
	print ("------------------------------------")
	await bot.change_presence(game=discord.Game(name=status,type=3))
	
##############################################################################################################################
# ℹ️ | A D M I N - C O M M A N D S
##############################################################################################################################

@bot.command(pass_context=True)
@commands.has_permissions(ban_members = True)
async def ban(ctx, user: discord.Member):
	embed = discord.Embed(title="Ban", description = f"{user.mention} has been banned by {ctx.message.author}", color=0x7289da,)
	embed.set_author(name="Bot Logs", icon_url=warning)
	seldel = await bot.say(embed=embed)
	await bot.ban(user)
	await asyncio.sleep(10)
	await bot.delete_message(selfdel)
	
@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unban(ctx, user: discord.Member):
	embed = discord.Embed(title="Unban", description="{0.name} has been unbanned from the server".format(user), color=0x7289da,)
	embed.set_author(name="Bot Logs", icon_url=warning)
	seldel = await bot.say(embed=embed)
	await bot.unban(user)
	await asyncio.sleep(10)
	await bot.delete_message(selfdel)
	
@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
	embed = discord.Embed(title="Kick", description="**{}** has been kicked from the server".format(user.name), color=0x7289da,)
	embed.set_author(name="Bot Logs", icon_url=warning)
	selfdel = await bot.say(embed=embed)
	await bot.kick(user)
	await asyncio.sleep(10)
	await bot.delete_message(selfdel)
	
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, msglimit : int):
	deleted = await bot.purge_from(ctx.message.channel, limit=msglimit)
	embed = discord.Embed(title="Clear", description='Cleared **{}** message(s) from the channel'.format(len(deleted)), color=0x7289da,)
	embed.set_author(name="Bot Logs", icon_url=warning)
	selfdel = await bot.say(embed=embed)
	await asyncio.sleep(10)
	await bot.delete_message(selfdel)

##############################################################################################################################
# ℹ️ | P I N G
##############################################################################################################################

@bot.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel   
	try:
	 t1 = time.perf_counter()
	 await bot.send_typing(channel)
	 ta = t1
	 t2 = time.perf_counter()
	 await bot.send_typing(channel)
	 tb = t2
	 ra = round((tb - ta) * 1000)
	finally:
	 pass
	try:
	 t1a = time.perf_counter()
	 await bot.send_typing(channel)
	 ta1 = t1a
	 t2a = time.perf_counter()
	 await bot.send_typing(channel)
	 tb1 = t2a
	 ra1 = round((tb1 - ta1) * 1000)
	finally:
	 pass
	try:
	 t1b = time.perf_counter()
	 await bot.send_typing(channel)
	 ta2 = t1b
	 t2b = time.perf_counter()
	 await bot.send_typing(channel)
	 tb2 = t2b
	 ra2 = round((tb2 - ta2) * 1000)
	finally:
	 pass
	try:
	 t1c = time.perf_counter()
	 await bot.send_typing(channel)
	 ta3 = t1c

	 t2c = time.perf_counter()
	 await bot.send_typing(channel)
	 tb3 = t2c

	 ra3 = round((tb3 - ta3) * 1000)
	finally:
	 pass
	try:
	 t1d = time.perf_counter()
	 await bot.send_typing(channel)
	 ta4 = t1d

	 t2d = time.perf_counter()
	 await bot.send_typing(channel)
	 tb4 = t2d

	 ra4 = round((tb4 - ta4) * 1000)
	finally:
	 pass

	embed = discord.Embed(color=0x7289da,)
	embed.set_author(name="Bot Connection", icon_url=dis_cord)
	embed.set_thumbnail(url=wave)
	embed.add_field(name='Ping 1', value=f"{str(ra)}ms", inline=True)
	embed.add_field(name='Ping 2', value=f"{str(ra2)}ms", inline=True)
	embed.add_field(name='Ping 3', value=f"{str(ra3)}ms", inline=True)
	embed.add_field(name='Ping 4', value=f"{str(ra4)}ms", inline=True)
	embed.set_footer(text=f"Requested by {ctx.message.author} | v{ver}", icon_url=ctx.message.author.avatar_url) 
	await bot.say(embed=embed)

##############################################################################################################################
# ℹ️ | V E R S I O N
##############################################################################################################################

@bot.command(pass_context=True)
async def version(ctx):
	embed = discord.Embed(title="Version", description=f"The current version of {botname} is: `{ver}`", color=0x7289da,)
	embed.set_author(name="Bot Logs", icon_url=warning)
	await bot.say(embed=embed)

##############################################################################################################################
# ℹ️ | W E B S I T E
##############################################################################################################################

# DISABLED

#@bot.command(pass_context=True)
#async def website(ctx):
	#embed = discord.Embed(color=0x7289da,)
	#embed.set_author(name="Website", icon_url=wave)
	#embed.add_field(name="Link:", value="https://relykxdiscord.wixsite.com/mikibot")
	#await bot.say(embed=embed)
	
##############################################################################################################################
# ℹ️ | D O N A T E
##############################################################################################################################

# DISABLED

#@bot.command(pass_context=True)
#async def donate(ctx):
	#embed = discord.Embed(description="You can donate here: \nhttps://www.patreon.com/join/vixendiscord?", color=0xf76754)
	#embed.set_author(name="Patreon", icon_url=patreon)
	#embed.set_thumbnail(url=patreon)
	#await bot.say(embed=embed)

##############################################################################################################################
# ℹ️ | P A S S W O R D
##############################################################################################################################

@bot.command(pass_context=True)
async def password(ctx):
	embed = discord.Embed(title=f"Password Generated", description=":mailbox_with_mail: Check DMs", color=0x7289da)
	embed.set_footer(text=f"Requested by {ctx.message.author} | v{ver}", icon_url=ctx.message.author.avatar_url)
	await bot.say(embed=embed)
	encryptkey = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
	encryptcode = ['1','2','3','4','5','6','7','8','9',]
	count1 = random.randint(1, 52)
	count2 = random.randint(1, 52)
	count3 = random.randint(1, 52)
	count4 = random.randint(1, 52)
	count5 = random.randint(1, 52)
	count6 = random.randint(1, 52)
	count7 = random.randint(1, 52)
	count8 = random.randint(1, 52)
	count9 = random.randint(1, 52)
	count10 = random.randint(1, 52)
	count11 = random.randint(1, 52)
	count12 = random.randint(1, 52)
	count13 = random.randint(1, 52)
	count14 = random.randint(1, 52)
	count15 = random.randint(1, 52)
	count16 = random.randint(1, 52)
	if count1 < 26:
	 key1 = (random.choice(encryptkey))
	if count1 >= 26: 
	 key1 = (random.choice(encryptcode))
	if count2 < 26:
	 key2 = (random.choice(encryptkey))
	if count2 >= 26: 
	 key2 = (random.choice(encryptcode))
	if count3 < 26:
	 key3 = (random.choice(encryptkey))
	if count3 >= 26: 
	 key3 = (random.choice(encryptcode))
	if count4 < 26:
	 key4 = (random.choice(encryptkey))
	if count4 >= 26: 
	 key4 = (random.choice(encryptcode))
	if count5 < 26:
	 key5 = (random.choice(encryptkey))
	if count5 >= 26: 
	 key5 = (random.choice(encryptcode))
	if count6 < 26:
	 key6 = (random.choice(encryptkey))
	if count6 >= 26: 
	 key6 = (random.choice(encryptcode))
	if count7 < 26:
	 key7 = (random.choice(encryptkey))
	if count7 >= 26: 
	 key7 = (random.choice(encryptcode))
	if count8 < 26:
	 key8 = (random.choice(encryptkey))
	if count8 >= 26: 
	 key8 = (random.choice(encryptcode))
	if count9 < 26: 
	 key9 = (random.choice(encryptkey))
	if count9 >= 26: 
	 key9 = (random.choice(encryptcode))
	if count10 < 26: 
	 key10 = (random.choice(encryptkey))
	if count10 >= 26: 
	 key10 = (random.choice(encryptcode))
	if count11 < 26: 
	 key11 = (random.choice(encryptkey))
	if count11 >= 26: 
	 key11 = (random.choice(encryptcode))
	if count12 < 26:
	 key12 = (random.choice(encryptkey))
	if count12 >= 26:
	 key12 = (random.choice(encryptcode))
	if count13 < 26:
	 key13 = (random.choice(encryptkey))
	if count13 >= 26:
	 key13 = (random.choice(encryptcode))
	if count14 < 26:
	 key14 = (random.choice(encryptkey))
	if count14 >= 26:
	 key14 = (random.choice(encryptcode))
	if count15 < 26:
	 key15 = (random.choice(encryptkey))
	if count15 >= 26:
	 key15 = (random.choice(encryptcode))
	if count16 < 26:
	 key16 = (random.choice(encryptkey))
	if count16 >= 26:
	 key16 = (random.choice(encryptcode))
# There are about ???,???,??? different password combinations that can be generated.
	encryptedpass = (key1 + key2 + key3 + key4 + key5 + key6 + key7 + key8 + key9 + key10 + key11 + key12 + key13 + key14 + key15 + key16)
	embed = discord.Embed(description='Here is your randomly generated password: ' + '`' + encryptedpass + '`', color=0x7289da)
	await bot.send_message(ctx.message.author, embed=embed)

##############################################################################################################################
# ℹ️ | W E L C O M E
##############################################################################################################################

@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def welcome(ctx):
	embed = discord.Embed(color=0x7289da,)
	embed.set_image(url="https://cdn.discordapp.com/attachments/535747082192027651/539772749091045376/welc.png")
	await bot.say(embed=embed)
	
	embed = discord.Embed(color=0x7289da,)
	embed.set_image(url=ctx.message.server.icon_url)
	await bot.say(embed=embed)
	
	embed = discord.Embed(description=f"Welcome to {ctx.message.server.name}!\nInvite your friends!", color=0x7289da,)
	await bot.say(embed=embed)
	
	#discinv = await bot.create_invite(destination = ctx.message.server.channel, max_age = 0, max_uses = 0)
	await bot.say('<:discord:535748146761039872> Invite: https://discord.gg/urtpruK')
	await bot.say('● Firstly please check out the <#538269485467959311> for all the legal information.\n● Also check out the <#538272649256632320> channel to register.\n● Lookout for notifications in <#538265451894145024> for new info.\n● If you have any problems, suggestions, or need any help feel free to ask the staff in <#538275130980171782>.\n● Lastly why not say "Hello" in the <#538265233190289410>.')
	
##############################################################################################################################
# ℹ️ | R U L E S
##############################################################################################################################

@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def rules(ctx):
	embed = discord.Embed(color=0x7289da,)
	embed.add_field(name="Rules", value="● Use common sense.\n● Do not advertise, regardless of here or DM.\n● Don't be rude.\n● No spam.\n● Respect the moderators.\n● Don't post any websites that are harmful, exposing, etc.\n● Please use the relevant channels provided.\n● There are no exceptions for being banned, even if you're a Moderator, Admin, etc.\n ‏‏‎ ", inline=False)
	embed.add_field(name="Temporary Rules", value=f"● {temprule}\n ‏‏‎ ", inline=False)
	embed.set_footer(text="Note: Do not attempt on making loopholes around the rules, that will result in either kick or ban regardless of the rule being here or not.")
	await bot.say(embed=embed)
	
##############################################################################################################################
# ℹ️ | S H O P
##############################################################################################################################

@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def shop(ctx):
	embed = discord.Embed(description="**`S` `H` `O` `P`**\n ‏‏‎ ", color=0x7289da,)
	embed.set_author(name=ctx.message.server.name, icon_url=ctx.message.server.icon_url)
	embed.add_field(name="10 Joins on your invite link", value="● To become a member of the server you need to invie 10 others and complete a profile in <#538272649256632320>.\n ‏‏‎ ", inline=False)
	embed.add_field(name="25 Joins on your invite link", value="● You get a role made just for you, with any name and color you want.\n ‏‏‎ ", inline=False)
	embed.add_field(name="50 Joins on your invite link", value="● A friend of your choice gets a custom role.\n ‏‏‎ ", inline=False)
	embed.add_field(name="100 Joins on your invite link", value="● A one time payment of $10 for 100 invited members.\n ‏‏‎ ", inline=False)
	embed.add_field(name="200 Joins on your invite link", value='● You get a custom role "gang" with any name you want. This role can have any color and name, and will appear separately. You can choose up to five of your friends  to be apart of this role "gang".\n ‏‏‎ ', inline=False)
	embed.add_field(name="@everyone Ping with an advertisement", value="● FREE - however, this price will rise in correlation to the member count.", inline=False)
	embed.add_field(name=" ‏‏‎ ", value="Check your invite count with `!invites` in <#539810655323029514>.\nDM Relykx#2896 once you meet the criteria, or are interested in buying.", inline=False)
	await bot.say(embed=embed)

##############################################################################################################################
# ℹ️ | B O T S
##############################################################################################################################

@bot.command()
@commands.has_permissions(administrator = True)
async def price(ctx):
	emb = discord.Embed(description="**`B` `O` `T` `S`**\n ‏‏‎ ", color=0x7289da,)
	emb.set_author(name=ctx.message.server.name, icon_url=ctx.message.server.icon_url)
	emb.add_field(name="WARN | MUTE | BAN | KICK", value="**US$22.75** [-32%]\n~~US$15.50~~\n ‏‏‎ ", inline=False)
	emb.add_field(name="ANTI SPAM", value="**US$11.40** [-32%]\n~~US$7.75~~\n ‏‏‎ ", inline=False)
	emb.add_field(name="MUSIC BOT", value="**US$17.10** [-32%]\n~~US$11.60~~\n ‏‏‎ ", inline=False)
	emb.set_footer(text="Note: All pricess are subject to change.")
	await ctx.send(embed=emb)
	
##############################################################################################################################
# ℹ️ | F A Q
##############################################################################################################################

@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def faq1(ctx):
	embed = discord.Embed(color=0x7289da,)
	embed.add_field(name="Q. What is this server?", value="A. This server is a comunity based on music development and streaming, we welcome everyone to participate or just watch and listen.", inline=False)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def faq2(ctx):
	embed = discord.Embed(color=0x7289da,)
	embed.add_field(name="Q. How do I become a moderator?", value="A. To become eligible for recruitment as a moderator you must have completed the 10 invite tier in the <#539809427520487444> and be active within the server.", inline=False)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def faq3(ctx):
	embed = discord.Embed(color=0x7289da,)
	embed.add_field(name="Q. How can I get verified?", value="A. To verify you need to send a pic of a valid ID to a verified staff member; ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ \n● You may blur out, Name, address and any other sensitive information. \n● You may not blur out your Picture or your DOB. \n● You may only verify with a <@&540016356515512331> or <@&538318193450680320>.", inline=False)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def faq4(ctx):
	embed = discord.Embed(color=0x7289da,)
	embed.add_field(name="Q. How do I get roles?", value="A. Go to <#538272649256632320> and react to each of the different categories to assign yourself to them.", inline=False)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def faq5(ctx):
	embed = discord.Embed(color=0x7289da,)
	embed.add_field(name="Q. Is this an 18+ server?", value="A. Yes and No! - As a new member the nsfw section of the server is hidden, once verified you will gain access if you pass registration.\n● `(Any sensitive media will cause an instant ban)`.\n● <#538265849463701514> & <#542506187313381407> however are nsfw but not for any form of pornography.", inline=False)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def faq6(ctx):
	embed = discord.Embed(color=0x7289da,)
	embed.add_field(name="Q. Do we do partnerships?", value="A. Yes, we do partnerships. Get in touch with one of our Partnership Managers, Staff Members, Moderators, Administrators, Managers, or Owners to get everything set up.", inline=False)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def faq7(ctx):
	embed = discord.Embed(color=0x7289da,)
	embed.add_field(name='Q. What does this "🚧" emoji mean?', value="A. When you see this emoji next to a channel it means it is under maintenance and will be up shortly.", inline=False)
	await bot.say(embed=embed)
	
bot.run(os.getenv("BOT_TOKEN"))
