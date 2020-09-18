#!/usr/bin/python3
"using reddit api"
import requests


def number_of_subscribers(subreddit):
    "number of subscribers"

    headers = {
        'authority': 'www.reddit.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
         AppleWebKit/537.36 (KHTML, like Gecko) \
         Chrome/85.0.4183.102 Safari/537.36',
        'accept':
        'text/html,application/xhtml+xml,\
        application/xml;q=0.9,image/avif,\
        image/webp,image/apng,*/*;q=0.8,\
        application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    if 'error' in response.json():
        return 0
    return response.json()["data"]["subscribers"]
