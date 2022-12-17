import os
import pymongo
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()


def db_connection():
    username = quote_plus(os.getenv("DB_USER_NAME"))
    password = quote_plus(os.getenv("DB_PASSWORD"))
    uri = f"mongodb+srv://{username}:{password}@cluster0.1sxtc.mongodb.net/?retryWrites=true&w=majority"
    return pymongo.MongoClient(uri)["itask"]


class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


class DataBaseInfo(Singleton):

    def __init__(self):
        self.client = db_connection()

    def all_tasks(self, language: str):
        return self.client[language]

    async def add_task_to_db(self, info: tuple, ctx: object):
        if len(info) != 3:
            await ctx.author.send("**Right format is:**```python 2_test_ http://test.com```")
            return

        language, task_name, url = info

        if language not in ("python", "java", "cs", "js"):
            await ctx.author.send("```Supported language`s are python, java, cs, js!!!```")
            return

        find_task = self.all_tasks(language).find_one({"$or": [{"task name": task_name}, {"task url": url}]})
        if find_task:
            await ctx.author.send(f"**The task already exists as:** ```name - {find_task['task name']}\nurl - {find_task['task url']}```")
            return

        self.all_tasks(language).insert_one({"task name": task_name, "task url": url})
        await ctx.author.send(f"```The task was added to Data Base for {language.capitalize()}!!!```")

    async def find_tasks(self, language: str, task_name: str):
        return list(self.all_tasks(language).find({"task name": {"$regex": task_name}}))
