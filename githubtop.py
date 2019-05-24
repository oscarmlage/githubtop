#!/usr/bin/env python

import json
import requests


if __name__ == '__main__':
    print('Github top')

    location = 'Lugo'

    filename = '{}.json'.format(location.lower())
    url = 'https://api.github.com/search/users?q=location:{}'.format(location)
    res = requests.get(url)

    with open(filename, 'w') as f:
        data = res.json()
        f.write(json.dumps(data))

    for i, user in enumerate(data['items'], 1):
        ev_url = 'https://api.github.com/users/{}/events'.format(user['login'])
        ev_data = requests.get(ev_url)
        print('%2d.- %s (%s)' % (i, user['login'], len(ev_data.json())))
