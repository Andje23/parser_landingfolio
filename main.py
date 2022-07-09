import requests
import json
import os
import time

from dataclasses import dataclass


# headers = {
#      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari"
#                    "/537.36",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
#               "application/signed-exchange;v=b3;q=0.9"
# }
# print(headers)


@dataclass(slots=True, frozen=True)
class Headers:
    user_agent: str
    accept: str


headers = Headers(user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/92.0.4515.159 Safari/537.36",
                  accept="text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;"
                         "q=0.8,application/signed-exchange;v=b3;q=0.9")


def get_data_file(headers: Headers):
    url = "https://www.landingfolio.com/"
    r = requests.get(url=url, headers={"User-Agent":headers.user_agent, "Accept":headers.accept})
    with open("index.html", "w") as file:
        file.write(r.text)