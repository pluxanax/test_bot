import json
import os

import requests

TOKEN = os.getenv('TOKEN')
URL = 'https://api.telegram.org/bot' + TOKEN + '/'


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def main():
    d = get_updates()
    with open('updates.json', 'w') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
