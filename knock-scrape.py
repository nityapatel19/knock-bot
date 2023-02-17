from typing import TypedDict, List

import requests
from bs4 import BeautifulSoup


class joke(TypedDict):
    id: int
    content: List[str]
    is_told: bool


BASE_URL = 'https://jokes.one'

with open('knock-knock.json', 'w') as f:
    library_endpoint = "tag/knock-knock"
    response = requests.get(BASE_URL + library_endpoint, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    pages = int(soup.find_all('a', class_='page-link')[-2].text)

    # for page in range(1, 2):
    #     response = requests.get(f"{BASE_URL}/{library_endpoint}/{page}")
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #
    #     jokes = soup.find_all('article', class_='row')
    #     for joke in jokes:
    #         joke = joke.find('a')
    #         print(joke['href'])
    #     print(f'Found {len(jokes)} jokes')
