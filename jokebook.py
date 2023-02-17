import json
import random
from typing import Optional

with open('config.json') as f:
    config = json.load(f)

JOKES_PATH = config['jokes']


def get_jokes() -> list:
    with open(JOKES_PATH) as f:
        return json.load(f)


def get_joke(joke_id: Optional[int] = None) -> dict:
    if joke_id is not None:
        return next(x for x in get_jokes() if x['id'] == joke_id)

    all_jokes = get_jokes()
    untold_jokes = list(filter(lambda x: not x['is_told'], all_jokes))

    if len(untold_jokes) == 0:
        for joke in all_jokes:
            joke['is_told'] = False
        untold_jokes = all_jokes

    random_joke = random.choice(untold_jokes)

    for joke in all_jokes:
        if joke == random_joke:
            joke['is_told'] = True
            break

    with open(JOKES_PATH, 'w+') as file:
        json.dump(all_jokes, file)

    return random_joke
