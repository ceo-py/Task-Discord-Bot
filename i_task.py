import json
from discord.ext import commands
from datetime import datetime
from text_cleaning.string_cleaning import StringCleaning as Sc
from buttons.language_bttons import LanguageButtons, discord, db_, os


class PersistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()

        super().__init__(command_prefix="?", help_command=None, intents=intents)

    async def setup_hook(self) -> None:
        self.add_view(LanguageButtons())


client = PersistentViewBot()

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
    "js": {
        "thumbnail url": "https://cdn.discordapp.com/attachments/983670671647313930/1056201559102476318/pngwing.com.png",
        "data": "js"
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


@client.command()
async def add(ctx):
    if str(ctx.author) in os.getenv("OWNER"):
        await ctx.send(embed=discord.Embed(
            colour=discord.Colour.blue(),
            title="** Click on language to add task in database ** :warning: "
        ), view=LanguageButtons())


async def show_result_message(task, ctx, language):
    if task:
        respond = await look_for_answer(task, language)
        if not respond:
            respond = "No results found.\nYou can use **?help** for more information."
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


@client.command(aliases=['py', "cs", "java", "js"])
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
    embed.add_field(name=f"?py task name - for Python\n?cs task name - for C#\n"
                         f"?java task name - for Java",
                    value=f"```fix\nWhen you ask me for a task by its full name "
                          f"(or at least part of its name) I will search for it and show you the results. "
                          f"If you are not sure how to ask me - see the example below.```[Command example]("
                          f"https://cdn.discordapp.com/attachments/983670671647313930/1056160608917131294/image.png)",
                    inline=False)
    embed.add_field(name=f"?help",
                    value=f"```fix\nHave no fear - I task is here! Oops - I have said that already, ain't I? "
                          f"Well...  if you see this, then you are looking at my ?help, so enjoy it!```",
                    inline=False)
    await ctx.author.send(embed=embed)


@client.command()
async def stats(ctx):
    if str(ctx.author) in os.getenv("OWNER"):
        with open("stats.json", "r", encoding='utf-8') as stats:
            data = json.load(stats)
            embed = discord.Embed(
                title=f":warning:Total Answers:warning:",
                description=f"{sum(data.values())}",
                colour=discord.Colour.blue()
            )

            await ctx.author.send(embed=embed)


async def look_for_answer(question, language):
    search_for = await Sc.clean_input(question)
    find_tasks = await db_.find_tasks(LANGUAGE_DATA[language]["data"], search_for)
    result = []

    for show in find_tasks:
        if sum(len(x) for x in result) <= 3850:
            result.append(f"[{await Sc.prepare_text_for_output(show['task name'])}]({show['task url']})")
        else:
            break

    return "\n".join(result)

client.run(os.getenv("TOKEN"))
