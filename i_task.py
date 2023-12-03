from discord.ext import commands

from buttons.searching_task_buttons import LanguageSearchingButtons
from buttons.language_buttons import LanguageButtons, discord, os
from prepare_answer.generate_message import show_result_message
# from show_task.show_task import ShowTask
from stats.add_stats_json import load_stats
from select_menus.select import Select, exams


class PersistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()

        super().__init__(command_prefix="?", help_command=None, intents=intents)

    async def setup_hook(self) -> None:
        self.add_view(LanguageButtons())
        self.add_view(LanguageSearchingButtons())


client = PersistentViewBot()
# ST = ShowTask()


@client.event
async def on_ready():
    # await client.tree.sync() # once only to sync add/remove new slash command
    await client.change_presence(activity=discord.Game(name="On your demand!!!"))
    print("Ready")


@client.command()
async def add(ctx):
    if str(ctx.author) in os.getenv("OWNER"):
        await ctx.send(
            embed=discord.Embed(
                colour=discord.Colour.blue(),
                title="** Click on language to add task in database ** :warning: ",
            ),
            view=LanguageButtons(),
        )


@client.command(aliases=["py", "cs", "java", "js", "html", "mssql"])
async def task(ctx, *task):
    if ctx.invoked_with == "task":
        await ctx.author.send(embed=embed_for_itask(), view=LanguageSearchingButtons())
        return

    await ctx.author.send(
        embed=await show_result_message(task, ctx.invoked_with, exams)
    )


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Have no fear - I task is here!",
        description="My master has taught few commands to aid you with your SoftUni coding adventure:",
        colour=discord.Colour.gold(),
    )
    embed.set_thumbnail(
        # url="https://cdn.discordapp.com/attachments/983670671647313930/994162444467445870"
        #     "/pnghut_customer-service-technical-support.png"
        url="https://github.com/ceo-py/Project-Pictures/blob/main/Itask/chat_icon.png?raw=true"
    )
    embed.add_field(
        name=f"?py task name - for Python\n?cs task name - for C#\n"
             f"?java task name - for Java\n"
             f"?js task name - for JavaScript\n"
             f"?html task name - for html and css\n"
             f"?mssql task name - for MS-MSQL",
        value=f"```fix\nWhen you ask me for a task by its full name "
              f"(or at least part of its name) I will search for it and show you the results. "
              f"If you are not sure how to ask me.```[Read More]("
              f"https://www.ceo-py.eu/DiscordBot/)",
        inline=False,
    )
    embed.add_field(
        name="/itask",
        value="```fix\nThis command will bring menu with all languages that currently are supported for "
              "task"
              "searching.```",
    )
    embed.add_field(
        name=f"?help",
        value=f"```fix\nHave no fear - I task is here! Oops - I have said that already, ain't I? "
              f"Well...  if you see this, then you are looking at my ?help, so enjoy it!```",
        inline=False,
    )
    await ctx.author.send(embed=embed)


@client.tree.command(name="rounding", description="Link with info about rounding!")
async def rounding(interaction: discord.Interaction):
    embed = discord.Embed(
        title="**Закръгление!!!**",
        description="При използване на **f2/2f/2** цифрата 2 представлява колко знака след "
                    "десетичната точка желаем да покажем! За всички езици когато желаем да е "
                    "до най-близкото цяло число **надолу (3.87 -> 3)** може да използваме директно INT. "
                    "При желание да покажете абсолютна стойност ползвайте **ABS (Math.abs / abs())**\n\n"
                    "**Python**```py\n"
                    "import math\n"
                    "x = 3.14159\n"
                    "print(f'{x:.2f}') # 3.14\n"
                    "print(math.floor(x)) # 3\n"
                    "print(math.ceil(x)) # 4```\n"
                    "**C#**```cs\n"
                    "double x = 3.14159;\n"
                    'Console.WriteLine($"{x:f2}"); // 3.14\n'
                    "Console.WriteLine(Math.Floor(x)); // 3\n"
                    "Console.WriteLine(Math.Ceiling(x)); // 4```\n"
                    "**JAVA**```java\n"
                    "double x = 3.14159;\n"
                    'System.out.printf("Total: %.2f", x); // 3.14\n'
                    "System.out.println(Math.floor(x)); // 3.0\n"
                    "System.out.println(Math.ceil(x)); // 4.0```\n"
                    "**JS**```js\n"
                    "let x = 3.14159;\n"
                    "console.log(x.toFixed(2)); // 3.14\n"
                    "console.log(Math.floor(x)); // 3\n"
                    "console.log(Math.ceil(x)); // 4```\n",
        colour=discord.Colour.gold(),
    )
    embed.set_thumbnail(
        # url="https://cdn.discordapp.com/attachments/983670671647313930/1068903570335879318/rounding_23.png"
        url="https://github.com/ceo-py/Project-Pictures/blob/main/Itask/rounding_23.png?raw=true"
    )
    await interaction.response.send_message(embed=embed)


@client.tree.command(
    name="percent", description="Link with info about calculating percents!"
)
async def percent(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Как да изчисляваме проценти!",
        description="**Подробна информация** [ТУК](https://www.kaksepravibg.com/kak-se-izchisliava-procent/?fbclid"
                    "=IwAR1vuZo1zZnaW0eAZnlhTT3ClPxMtojowO1Y9ORzrqc1OfH4-3XSTe-PjcY)",
        colour=discord.Colour.gold(),
    )
    embed.set_thumbnail(
        #     url="https://cdn.discordapp.com/attachments/983670671647313930/1061681874239500358/pngegg_1.png"
        # )
        url="https://github.com/ceo-py/Project-Pictures/blob/main/Itask/percent.png?raw=true"
    )
    embed.add_field(
        name="**Пример: 1**",
        value="Имаме 10 ябълки. 10 ябълки са 100%. Изяждаме 2 ябълки. От тук следва, че сме изяли **__2 / 10 х 100% = "
              "20%__**"
              "от ябълките и оставаме с 80% от първоначалния брой ябълки."
              " От този пример можем да изведем формулата за смятане на процент от число"
              " процент от цяло = **__част х 100 / цялото__**"
              " или в нашия пример:"
              " **__20%  = 2 ябълки х 100  / 10 ябълки__**",
        inline=False,
    )
    embed.add_field(
        name="**Пример: 2**",
        value="Имаме промоция 8% на стока на цена 200 лв. Използваме следната формула:"
              " **__200 х 8 / 100 = 16 лв__**. Следователно цената на стоката е 184 лв.",
        inline=False,
    )
    embed.add_field(
        name="**Пример: 3**",
        value="**98 * 0.9 = 88.2** - Намаляме числото 98 с 10%.\n"
              "**98 * 0.73 = 71.54** - Намаляме числото 98 с 27%.\n"
              "Видно от примерa за намалениe числото започва с 0. "
              "след това процента с които желаете да намалите числото ако е примерно 15%. "
              "100 - 15 = 85 или 0.85 * желаното число.\n"
              "**98 * 1.10 = 107.8** - Увеличаваме числото 98 с 10%.\n"
              "**98 * 1.35 = 132.3** - Увеличаваме числото 98 с 35%.\n"
              "За увеличение число започва с 1. "
              "след това процента с които желаем да направим увеличението. "
              "Примерно 47% ще бъде 1.47 * желаното число.",
        inline=False,
    )
    embed.add_field(
        name="**Намиране на число по даден процент**",
        value="Ако сме закупили стока, намалена с 20% и сме платили цена от 160 лв, колко е била цената на стоката "
              "без намалението. Намалението е било 20%, следователно сме платили 80% от цената на стоката. Стоката е "
              "струвала Х лева. Смятаме по формулата: **__80 / 100 * Х = 160__** Като пресметнем уравнението, "
              "се получава, че цената преди намалението е била 200 лв.",
        inline=False,
    )
    await interaction.response.send_message(embed=embed)


@client.tree.command(
    name="itask", description="It will show you how to use the bot for task solutions."
)
async def itask(interaction: discord.Interaction):
    embed = embed_for_itask()

    await interaction.response.send_message(
        embed=embed, view=LanguageSearchingButtons()
    )

    # responses in channel
    # await interaction.user.send(
    #     embed=embed, view=LanguageSearchingButtons()
    # )


@client.tree.command(
    name="logsolution", description="Possible solutions to sing in SoftUni web site."
)
async def logsolution(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Предложения за логване в сайта на СофтУни при проблем.",
        description="Ако сте сигурни, че сайта който се опитвате да достъпите не е в профилактика, опитайте следното:",
        colour=discord.Colour.gold(),
    )
    embed.set_thumbnail(
        #     url="https://cdn.discordapp.com/attachments/983670671647313930/1113488543235453061/pngwing.com.png"
        # )
        url="https://github.com/ceo-py/Project-Pictures/blob/main/Itask/help_icon.png?raw=true"
    )
    embed.add_field(
        name="**Отворете с друг Браузър**",
        value="Примерно ползвате Google Chrome опитайте да го отворите с някой от следните браузъри: Firefox, Microsoft Edge, Opera, Brave etc."
              "Проблема продължава опитайте:",
        inline=False,
    )
    embed.add_field(
        name="**Изтрийте бисквитките/кеша от вашия Браузър**",
        value="Инструкция за изтриване на бисквитки/кеш за следните браузъри може да намерите както следва:\n"
              "[Google - Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop&oco=1)\n"
              "[Firefox - Mozilla](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)\n"
              "[Microsoft - Edge](https://support.microsoft.com/en-us/microsoft-edge/delete-cookies-in-microsoft-edge-63947406-40ac-c3b8-57b9-2a946a29ae09#:~:text=Select%20Settings%20%3E%20Privacy%2C%20search%2C,and%20then%20select%20Clear%20now.)\n"
              "[Opera](https://blogs.opera.com/tips-and-tricks/2023/04/clean-browser-and-remove-trackers/)\n"
              "[Brave](https://brave.com/learn/how-to-delete-search-history/#:~:text=Delete%20your%20browsing%20history%20on%20Brave&text=Open%20Brave.,history%20you%20want%20to%20delete.)\n"
              "Ползвате друг браузър от изброените по-горе потърсете в гугъл.",
        inline=False,
    )
    embed.add_field(
        name="**Все още не може да се логнете**",
        value="Тук ще намерите начините за контакт със СофтУни https://discord.com/channels/954298970799243285/954298972158173211",
        inline=False,
    )
    await interaction.response.send_message(embed=embed)


@client.command()
async def stats(ctx):
    if str(ctx.author) in os.getenv("OWNER"):
        data = await load_stats()
        embed = discord.Embed(
            title=f":warning:Total Answers:warning:",
            description=f"{sum(data.values())}",
            colour=discord.Colour.blue(),
        )
        await ctx.author.send(embed=embed)


def embed_for_itask():
    embed = discord.Embed(
        title="Показвам примерни решения на задачите от СофтУни!",
        description="Изберете езика за който желаете да намерите пример и напишете името на задача.\n"
                    "Ако желаете може да ми задавате въпроси на лично съобщение <@970393820497838180> с команда за съответния език "
                    "`?py`, `?cs`, `?java`, `?js`, `?html` или `?mssql` и името на задачата.",
        colour=discord.Colour.gold(),
    )
    return embed


def embed_for_itask_exam():
    embed = discord.Embed(
        title="Провеждат се изпити към момента!!!",
        description="С цел да се осигури нормалното протичане на изпитите, бота няма да дава отгорови до приключването им.\n"
                    "Благодаря за разбирането и успех на изпита!",
        colour=discord.Colour.red(),
    )
    return embed


@client.tree.command(name="exam")
async def test(interaction: discord.Interaction):
    if str(interaction.user) in os.getenv("OWNER") or str(
            interaction.user
    ) in os.getenv("PERMIT"):
        await interaction.response.send_message(view=Select())


# @client.tree.command(name="showtask", description="Available Task Solution")
# async def show(interaction: discord.Interaction, language: ST.languages(), module: ST.modules(), course: ST.course(), task: ST.task()):
#
#         await interaction.response.send_message(f'{language}, {module}, {course}, {task}')


client.run(os.getenv("TOKEN"))
