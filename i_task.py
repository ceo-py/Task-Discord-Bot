import discord
import os
import json
import string
from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime

load_dotenv()
TOKEN = os.getenv("TOKEN")
client = commands.Bot(command_prefix="?", help_command=None)

LANGUAGE_DATA = {
    "cs": {
        "thumbnail url": "https://cdn.discordapp.com/attachments/983670671647313930/1019383803535446096/pngegg.png",
        "data": "cs"
    },
    "py": {
        "thumbnail url": "https://cdn.discordapp.com/attachments/983670671647313930/994020525410111578/kisspng-python-"
                "general-purpose-programming-language-comput-python-programming-language-symphony-solution-"
                "5b6ee0c89ecd95.2067324515339931606505.png",
        "data": "python"
    },
    "java": {
        "thumbnail url": "https://cdn.discordapp.com/attachments/983670671647313930/1052942041652404256/java.png",
        "data": "java"
    },
}


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='On your demand!!!'))
    print("Ready")


async def add_stats():
    with open("stats.json", "r", encoding='utf-8') as stats:
        data = json.load(stats)

    current_month = datetime.now().month
    current_year = datetime.now().year

    data[f"{current_month} - {current_year}"] = data.get(f"{current_month} - {current_year}", 0) + 1
    with open("stats.json", "w", encoding='utf-8') as x:
        json.dump(data, x, indent=9)


async def clean_input(data):
    search_for = ' '.join(data)
    search_for = search_for.rstrip().lstrip().replace(". ", "_").replace(" ", "_") \
        .replace("-", "_").replace("'", "").lower()
    if search_for.startswith("0"):
        search_for = search_for.replace("0", "")
    return search_for


async def prepare_text_for_output(text):
    return string.capwords(text.replace("_", " "))


async def loading_answers_data(language: str):
    with open(f"{language}_data.json", "r", encoding='utf-8') as json_file:
        return json.load(json_file)


async def look_for_answer(question, language):
    data_info = await loading_answers_data(LANGUAGE_DATA[language]["data"])
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


async def show_result_message(task: str, ctx, language: str):
    if task:
        respond = await look_for_answer(task, language)
        if not respond:
            respond = "No results found.\nYou can use ?help for more information."
        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title="**Answers I found:**",
            description=f"{respond}"
        )
        embed.set_thumbnail(
            url=LANGUAGE_DATA[language]["thumbnail url"])

        await ctx.author.send(embed=embed)
    else:
        embed = discord.Embed(
            title=f":warning:You forget to ask for task:warning:",
            colour=discord.Colour.blue()
        )
        embed.add_field(name=f"**Examples:**:point_down:", value=f"```fix\n"
                                                                f"?{language} 9 Palindrome Integers\n"
                                                                f"?{language} 9 Palindrome\n"
                                                                f"?{language} Palindrome```",
                        inline=True)
        await ctx.author.send(embed=embed)
    await add_stats()


@client.command(aliases=['py', "cs", "java"])
async def task(ctx, *task):
    await show_result_message(task, ctx, ctx.invoked_with)


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Have no fear - I task is here!",
        description="My master has taught me two commands to aid you with your SoftUni coding adventure:",
        colour=discord.Colour.gold()
    )
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/983670671647313930/994162444467445870"
            "/pnghut_customer-service-technical-support.png")
    embed.add_field(name=f"?task or py [task name] - Python\ncs [task name] - for C#",
                    value=f"```fix\nWhen you ask me for a task by its full name "
                          f"(or at least part of its name) I will search for it and show you the results. "
                          f"If you are not sure how to ask me - see the example below.```[Command example]("
                          f"https://cdn.discordapp.com/attachments/983670671647313930/1018789872347131904/unknown.png)",
                    inline=False)
    embed.add_field(name=f"?help",
                    value=f"```fix\nHave no fear - I task is here! Oops - I have said that already, ain't I? "
                          f"Well...  if you see this, then you are looking at my ?help, so enjoy it!```",
                    inline=False)
    await ctx.author.send(embed=embed)


@client.command()
async def stats(ctx):
    with open("stats.json", "r", encoding='utf-8') as stats:
        data = json.load(stats)
        embed = discord.Embed(
            title=f":warning:Total Answers:warning:",
            description=f"{sum(list(data.values()))}",
            colour=discord.Colour.blue()
        )

        await ctx.author.send(embed=embed)


client.run(TOKEN)
