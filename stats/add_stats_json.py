import json
from datetime import datetime


async def add_stats():
    with open("stats.json", "r", encoding="utf-8") as stats:
        data = json.load(stats)

    current_month = datetime.now().month
    current_year = datetime.now().year

    data[f"{current_month} - {current_year}"] = (
        data.get(f"{current_month} - {current_year}", 0) + 1
    )
    with open("stats.json", "w", encoding="utf-8") as x:
        json.dump(data, x, indent=9)


async def load_stats():
    with open("stats.json", "r", encoding="utf-8") as stats:
        return json.load(stats)
