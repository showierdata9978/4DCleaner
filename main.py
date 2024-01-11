import nextcord
import dotenv

config = dotenv.dotenv_values(".env")

bot = nextcord.Client()

SLOWMODE_TIME= 60 * 60 * 6 # 6 hours

@bot.event
async def on_message(message: nextcord.Message):
    if message.author.bot:
        return

    if message.author.guild_permissions.manage_messages:
        return # skip mods

    if message.channel.category_id != int(config["ARCHIVED"]):
        return

    if message.channel.slowmode_delay < SLOWMODE_TIME:
        await message.channel.edit(slowmode_delay=SLOWMODE_TIME)

    await message.delete()

@bot.slash_command(guild_ids=[int(config["GUILD_ID"])])
async def about(ctx: nextcord.Interaction):
    embed = nextcord.Embed(title="About", description="This bot was made to fix misconfigured archive channels", color=nextcord.Color.blurple())
    embed.add_field(name="Author", value="ShowierData9978#0001", inline=False)
    embed.add_field(name="Source Code", value="[GitHub](https://github.com/showierdata9978/4DCleaner)", inline=False)

    await ctx.response.send_message(embed=embed)

bot.run(config["TOKEN"])