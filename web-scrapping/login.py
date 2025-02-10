import requests
from bs4 import BeautifulSoup

import os


def login(payload: dict):

    login_url = os.environ.get("LOGIN_URL")
    secure_url = os.environ.get("SECURE_URL")

    with requests.session() as s:
        s.post(login_url, data=payload)
        r = s.get(secure_url)
        soup = BeautifulSoup(r.content, "html.parser")

        return soup


if __name__ == "__main__":
    ...