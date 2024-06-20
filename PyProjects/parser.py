import json
from abc import ABC, abstractmethod

import requests

st_accept = "text/html"

st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
}
class Parser():
    st_accept = "text/html"

    st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

    headers = {
        "Accept": st_accept,
        "User-Agent": st_useragent
    }

    def __init__(self):
        pass

    @staticmethod
    def par(headers):
        r = requests.get("https://api.hh.ru/vacancies", headers=headers)
        pretty = json.dumps(r.json(), indent=2, ensure_ascii=False)
        print(pretty)
q = Parser
q.par(headers)

