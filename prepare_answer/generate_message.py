import discord
from prepare_answer.looking_for_answer import look_for_answer
from stats.add_stats_json import add_stats

LANGUAGE_DATA = {
    "cs": {
        "thumbnail url": "https://cdn.discordapp.com/attachments/983670671647313930/1019383803535446096/pngegg.png",
        "data": "cs",
    },
    "py": {
        "thumbnail url": "https://cdn.discordapp.com/attachments/983670671647313930/994020525410111578/kisspng-python-"
        "general-purpose-programming-language-comput-python-programming-language-symphony-solution-"
        "5b6ee0c89ecd95.2067324515339931606505.png",
        "data": "python",
    },
    "java": {
        "thumbnail url": "https://cdn.discordapp.com/attachments/983670671647313930/1052942041652404256/java.png",
        "data": "java",
    },
    "js": {
        "thumbnail url": "https://cdn.discordapp.com/attachments/983670671647313930/1056201559102476318/pngwing.com.png",
        "data": "js",
    },
    "html": {
        "thumbnail url": "https://cdn.discordapp.com/attachments/983670671647313930/1061697692587266158/pngfind.com-javascript-logo-png-1506020.png",
        "data": "html_css",
    },
    "mssql": {
        "thumbnail url": "https://cdn.discordapp.com/attachments/983670671647313930/1070267493379227729/pngwing.com.png",
        "data": "mssql",
    },
}


async def show_result_message(task, language, skip_moduls):

    if task:
        respond = await look_for_answer(task, LANGUAGE_DATA[language]["data"], skip_moduls)
        if not respond:
            respond = "No results found.\nYou can use **?help** for more information."
        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title="**Answers I found:**",
            description=f"{respond}",
        )
        embed.set_thumbnail(url=LANGUAGE_DATA[language]["thumbnail url"])

    else:
        embed = discord.Embed(
            title=f":warning:You forget to ask for task:warning:",
            colour=discord.Colour.blue(),
        )
        embed.add_field(
            name=f"**Examples:**:point_down:",
            value=f"```fix\n"
            f"?{language} 9 Palindrome Integers\n"
            f"?{language} 9 Palindrome\n"
            f"?{language} Palindrome```",
            inline=True,
        )
    await add_stats()
    return embed
