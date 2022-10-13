from requests_html import HTMLSession
import json

url_start = "https://github.com/AlexanderRVulchev/SoftUni-ProgrammingBasics"
session = HTMLSession()


def getdata(url):
    r = session.get(url)
    return r


htmldata = getdata(url_start)
my_links = []
links_for_bd = {}
check_url = {}


def get_all_directories(url_start):
    htmldata = getdata(url_start)
    links = htmldata.html.absolute_links

    for info in links:
        if "/tree/main/" in info != check_url.get(info):
            check_url[info] = info
            get_all_directories(info) #
        elif "Program.cs" in info:
            end = info.rfind("/")
            info_key = info[:end]
            end = info_key.rfind("/") + 1
            info_key = info_key[end:]
            print(info_key)
            if info_key.startswith("0"):
                info_key = info_key.replace("0", "", 1)
            for x, y in (("%20", " "), (".", " "), ("`", ""), ("%2B", "")):
                info_key = info_key.replace(x, y)
            info_key = " ".join(info_key.split())
            info_key = info_key.replace(" ", "_").lower()
            print(info_key)
            print(info)
            links_for_bd[info_key] = info


def write_json(data, filename="cs_data.json"):
    with open(filename, "w", encoding='utf-8') as x:
        json.dump(data, x, indent=9)


get_all_directories(url_start)


with open("cs_data.json", "r+", encoding='utf-8') as json_file:
    data = json.load(json_file)
    data_info = data
    data_info.update(links_for_bd)

write_json(data)

print(len(links_for_bd))


'''
1. Diagonal Difference
'''

'''
1.%20Diagonal%20Difference
'''