from requests import get as rget, head as rhead, post as rpost, Session as rsession
import math
import re
from re import findall as re_findall, sub as re_sub, match as re_match, search as re_search
from urllib.parse import urlparse, unquote
from json import loads as jsonloads
from lk21 import Bypass
from cfscrape import create_scraper
from bs4 import BeautifulSoup
from base64 import standard_b64encode
from time import sleep
import cloudscraper
import hashlib
import requests
import os



def mdisk(url):
    
    header = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://mdisk.me/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    	 }

    id = url.split("/")[-1]
    URL = f'https://diskuploader.entertainvideo.com/v1/file/cdnurl?param={id}'
    return requests.get(url=URL, headers=header).json()['source']
