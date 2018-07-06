#!/usr/bin/env python

import sys
import requests
import json
import subprocess

if sys.version_info[0] < 3:
    from exceptions import Exception
else:
    from builtins import Exception


def get_link(session, channel):
    session.headers.update({
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'pragma': 'no-cache',
        'origin': 'https://www.mitele.es',
        'accept-encoding': 'gzip',
        'accept-language': 'es-ES,es;q=0.9,ca;q=0.8,en;q=0.7',
    })

    request_headers = {
        'referer': 'https://www.mitele.es/live/index.html?alias=' + channel,
        'authority': 'indalo.mediaset.es',
        'accept': 'application/json',
    }

    r = session.get('https://indalo.mediaset.es/mmc-player/api/mmc/v1/'+ channel +'/live/html5.json', headers=request_headers)

    if r.status_code != 200:
        raise Exception(r.status_code, "Error {}, message: {}".format(r.status_code, r.text.encode('utf-8')))

    live_info = json.loads(r.text.encode('utf-8'))

    location = live_info['locations'][0]

    request_headers = {
        'referer': 'https://www.mitele.es/live/index.html?alias=' + channel,
        'authority': 'gatekeeper.mediaset.es',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json;charset=UTF-8'
    }

    payload = {
        'sta': 0,
        'gcp': location['gcp'],
        'ogn': location['ogn']
    }

    r = session.post("https:" + location['gat'], headers=request_headers, data=json.dumps(payload))

    if r.status_code != 200:
        raise Exception(r.status_code, "Error {}, message: {}".format(r.status_code, r.text.encode('utf-8')))

    stream_info = json.loads(r.text.encode('utf-8'))

    if not stream_info['stream']:
        raise Exception(1, "No stream returned")

    return stream_info['stream']


if __name__ == '__main__':

    with requests.Session() as s:
        if len(sys.argv) > 1:
            print(get_link(s, sys.argv[1]))

        else:
            channels = ['telecinco', 'cuatro', 'boing', 'divinity', 'fdf', 'energy', 'bemad', 'futbol-mitele']

            print("Channels\n")
            for i, c in enumerate(channels):
                print(str(i) + '\t' + c)

            channel = channels[int(input('\nEnter channel index: '))]

            subprocess.call(["mpv", get_link(s, channel)])
