import os
import asyncio
from os import getenv, environ
from asyncio import TimeoutError
from shortzy import Shortzy
from config import SITE , API_KEY

API_KEY = str(getenv('API_KEY', 'e0867ce24e2238645541bf7651be2217b4cd5dd1'))
SITE = str(getenv('SITE', 'shorturllink.in'))


shortzy = Shortzy(API_KEY, SITE)

async def get_shortlink(link):
    if not API_KEY or not SITE:
        return link

    try:
        x = await shortzy.convert(link, silently_fail=True)
    except Exception:
        x = await get_shortlink_sub(link)
    return x


async def get_shortlink_sub(link):
    url = f'https://{SITE}/api'
    params = {'api': API_KEY, 'url': link}
    scraper = cloudscraper.create_scraper() 
    r = scraper.get(url, params=params)
    return r.json()["shortenedUrl"]
