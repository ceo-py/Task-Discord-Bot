import discord
import os
import json
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("TOKEN")
client = commands.Bot(command_prefix="?", help_command=None)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='On your demand!!!'))
    print("Ready")


async def look_for_answer(question):
    with open("data.json", "r+", encoding='utf-8') as json_file:
        data = json.load(json_file)
        data_info = data["task"][0]
    search_for = ' '.join(question)
    search_for = search_for.rstrip().lstrip().replace(". ", "_").replace(" ", "_").replace("-", "_").lower()
    if search_for.startswith("0"):
        search_for = search_for.replace("0", "")
    try:
        url = data_info[search_for]
        return f"[{search_for}]({url})"

    except KeyError:
        result = ""
        for task, url in data_info.items():
            if search_for[3:6] in task and len(result) < 800:
                result += f"[{task}]({url})\n"
        return result


@client.command()
async def task(ctx, *task):
    if task:
        respond = await look_for_answer(task)
        embed = discord.Embed(
            title=f"Answers i found:",
            colour=discord.Colour.blue()
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/983670671647313930/994020525410111578/kisspng-python-"
                "general-purpose-programming-language-comput-python-programming-language-symphony-solution-"
                "5b6ee0c89ecd95.2067324515339931606505.png")

        embed.add_field(name=f":school::technologist::point_down:", value=f"**{respond}**", inline=True)
        await ctx.author.send(embed=embed)


client.run(TOKEN)
