import discord
import os
import json
import string
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("TOKEN")
client = commands.Bot(command_prefix="?", help_command=None)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='On your demand!!!'))
    print("Ready")


async def clean_input(data):
    search_for = ' '.join(data)
    search_for = search_for.rstrip().lstrip().replace(". ", "_").replace(" ", "_") \
        .replace("-", "_").replace("'", "").lower()
    if search_for.startswith("0"):
        search_for = search_for.replace("0", "")
    return search_for


async def prepare_text_for_output(text):
    return string.capwords(text.replace("_", " "))


async def loading_answers_data():
    with open("data.json", "r", encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data["task"][0]


async def look_for_answer(question):
    data_info = await loading_answers_data()
    search_for = await clean_input(question)
    output_text = await prepare_text_for_output(search_for)
    result = ""
    try:
        url = data_info[search_for]
        result = f"[{output_text}]({url})"

    except KeyError:
        for task, url in data_info.items():
            if len(result) <= 3850:
                output_text = await prepare_text_for_output(task)
                if search_for[0].isdigit():
                    if search_for[2:6] in task:
                        result += f"[{output_text}]({url})\n"
                else:
                    if search_for[:5] in task:
                        result += f"[{output_text}]({url})\n"
            else:
                break

    return result


@client.command()
async def task(ctx, *task):
    if task:
        respond = await look_for_answer(task)
        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title="**Answers i found:**",
            description=f"{respond}"
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/983670671647313930/994020525410111578/kisspng-python-"
                "general-purpose-programming-language-comput-python-programming-language-symphony-solution-"
                "5b6ee0c89ecd95.2067324515339931606505.png")

        await ctx.author.send(embed=embed)
    else:
        embed = discord.Embed(
            title=f":warning:You forget to ask for task:warning:",
            colour=discord.Colour.blue()
        )
        embed.add_field(name=f"**Example:**:point_down:", value=f"```fix\n"
                                                                f"?task 04. Palindrome Strings```", inline=True)
        await ctx.author.send(embed=embed)


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Bot Commands",
        description="I task is a bot with two commands, made to help you find solutions "
                    "on your coding journey from SoftUni.",
        colour=discord.Colour.gold()
    )
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/983670671647313930/994162444467445870"
            "/pnghut_customer-service-technical-support.png")
    embed.add_field(name=f"?task [task name]",
                    value=f"```fix\nWith that command you can ask for specific task. Simply copy the task name from judge and paste it, "
                          f"that will show you the solution if it`s found. Check the example below. ```[Command example]("
                          f"https://cdn.discordapp.com/attachments/983670671647313930/994164354079539282/unknown.png)",
                    inline=False)
    embed.add_field(name=f"?help",
                    value=f"```fix\nThat`s what you are looking at the moment.Enjoy it!!!```",
                    inline=False)
    await ctx.author.send(embed=embed)


client.run(TOKEN)
