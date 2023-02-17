import json

ALL_JOKES = './knock-knock.json'
BAD_JOKES = './bad_jokes.json'

with open(ALL_JOKES) as f1, open(BAD_JOKES, 'w') as f2:
    jokes = json.load(f1)
    bad_jokes = []
    for joke in jokes:
        if type(joke['id']) != int or type(joke['content']) != list or type(joke['is_told']) != bool:
            bad_jokes.append(joke)

        for i in range(len(joke['content'])):
            if type(joke['content'][i]) != str:
                bad_jokes.append(joke)
                break

            if i == 0 and not ('knock knock' in joke['content'][i].lower() or 'knock, knock' in joke['content'][
                i].lower() or 'knock-knock' in joke['content'][i].lower()):
                bad_jokes.append(joke)
                break

    json.dump(bad_jokes, f2)
