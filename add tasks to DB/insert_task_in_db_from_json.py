import json
import os
import pymongo
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

FILE = "js"


def db_connection():
    username = quote_plus(os.getenv("DB_USER_NAME"))
    password = quote_plus(os.getenv("DB_PASSWORD"))
    uri = f"mongodb+srv://{username}:{password}@cluster0.1sxtc.mongodb.net/?retryWrites=true&w=majority"
    return pymongo.MongoClient(uri)["itask"][FILE]


db_ = db_connection()

with open(f"{FILE}.json", "r+", encoding="utf-8") as json_file:
    # data = json.load(json_file)

    # for task_name, url in data.items():
    #
    #     find_task = db_.find_one(
    #         {"$or": [{"task name": task_name}, {"task url": url}]}
    #     )
    #     if not find_task:
    #         db_.insert_one({"task name": task_name, "task url": url})

    [
        db_.insert_one({"task name": task_name, "task url": url})
        for task_name, url in json.load(json_file).items()
        if db_.find_one({"$or": [{"task name": task_name}, {"task url": url}]})
    ]
