from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ui import Button, View
from tarkov import get_item_data, get_tier, get_color
from datetime import datetime
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

currency = "\u20BD"
greaterorequal = '\u2265'

@tree.command(name="tier", description="Tiers are assigned using slot price identification")
async def tier(interaction: discord.Interaction):
    embed = discord.Embed(title="Loot Tiers", color=0x000000)
    embed.add_field(name=":star:Legendary", value=f"{greaterorequal} 40 000{currency}", inline=False)
    embed.add_field(name=":green_circle:Great", value=f"{greaterorequal} 30 000{currency}", inline=False)
    embed.add_field(name=":yellow_circle:Average", value=f"{greaterorequal} 20 000{currency}", inline=False)
    embed.add_field(name=":red_circle:Poor", value=f"{greaterorequal} 10 000{currency}", inline=False)
    embed.add_field(name=":x:Trash", value=f"< 10 000{currency}",  inline=False)
    await interaction.response.send_message(embed=embed)      

@tree.command(name="how2use", description="Information about usage of the bot")
async def how2use(interaction: discord.Interaction):
    embed = discord.Embed(title="Fence Flea Market Keeper Tutorial", color=0x000000)
    embed.add_field(name="/price", value="This command allows you to check the actual market price of item", inline=False)
    embed.add_field(name="/tier", value="This command showing you, how tiers are given to items",  inline=False)
    await interaction.response.send_message(embed=embed) 

@tree.command(name="price", description="Check the price of Escape from Tarkov items")
async def price(interaction: discord.Interaction, search: str):
    try:
        item_data = get_item_data(search)
        item_name = item_data['name']
        item_price = item_data['low24hPrice']
        item_last48 =item_data['changeLast48hPercent']
        item_icon = item_data['iconLink']
        item_link = item_data['wikiLink']
        item_width = item_data['width']
        item_height = item_data['height']
        item_update = item_data['updated']
        date = datetime.fromisoformat(item_update)
        formatted_date = date.strftime("%d %B %Y, %H:%M:%S")
        slots = item_width*item_height
        price_perslot = item_price//slots
        slots1 = "slots"
        format_price = format(item_price,',')
        format_priceperslot = format(price_perslot, ',')
        if slots == 1:
            slots1 = "slot"
        button = Button(label="TarkovWiki", style=discord.ButtonStyle.green, url=item_link)
        view = View()
        view.add_item(button)
        embed = discord.Embed(title=f"{item_name}", color=get_color(price_perslot))
        embed.set_thumbnail(url=item_icon)
        embed.add_field(name="Price:", value=f' > {format_price}{currency}\n > (lowest price)', inline=True)
        embed.add_field(name="Per Slot:", value=f' > {format_priceperslot}{currency}\n > ({slots} {slots1})', inline=True)
        embed.add_field(name="Difference:", value=f' > 48h change:\n > {item_last48}% ', inline=True)
        embed.add_field(name="Tier:", value=get_tier(price_perslot), inline=False)
        embed.add_field(name="Last update:", value=formatted_date, inline=False)
        embed.set_footer(text="Data povided by: https://tarkov.dev/api/")
        await interaction.response.send_message(embed=embed, view=view)
    except Exception as e:
        embed = discord.Embed(title="Error", description=str(e), color=0xFF0000)
        await interaction.response.send_message(embed=embed)


@client.event
async def on_ready():
    await tree.sync()
    await client.change_presence(status=discord.Status.online, activity=discord.Game("/how2use | Fence "))
    print(f'you have successfully logged out of the {client.user}')

client.run(os.getenv("TOKEN"))
