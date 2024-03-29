from requests_html import HTMLSession
import json

url_start = "https://github.com/ceo-py/JS-Front-End"
session = HTMLSession()
FILE_EXTENSION = ".js"
FILE = "js"
SYMBOLS_BEHIND_EXTENSIONS = -len(FILE_EXTENSION)


def getdata(url):
    r = session.get(url)
    return r


htmldata = getdata(url_start)
my_links = []
check_url = {}


def get_all_directories(url_start):
    htmldata = getdata(url_start)
    links = htmldata.html.absolute_links
    for info in links:
        if "/tree/master/" in info != check_url.get(info):
            check_url[info] = info
            get_all_directories(info)
        elif info.endswith(FILE_EXTENSION):
            my_links.append(info)


def write_json(data, filename=f"{FILE}.json"):
    with open(filename, "w", encoding="utf-8") as x:
        json.dump(data, x, indent=9)


links_for_bd = {}
get_all_directories(url_start)
for task in my_links:
    print(task)
    taks_start_index = task.rfind("/") + 1
    task_name = task[taks_start_index:SYMBOLS_BEHIND_EXTENSIONS]
    links_for_bd[task_name] = task
    print(task_name)

with open(f"{FILE}.json", "r+", encoding="utf-8") as json_file:
    data = json.load(json_file)
    data.update(links_for_bd)

write_json(data)

print(len(my_links))
