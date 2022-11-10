import re
from re import match as rematch, findall, sub as resub
import requests
from requests import get as rget
import base64
from urllib.parse import unquote, urlparse, parse_qs
import time
import cloudscraper
from bs4 import BeautifulSoup, NavigableString, Tag
from lxml import etree
import hashlib
import json
from dotenv import load_dotenv
load_dotenv()
from asyncio import sleep as asleep
import PyBypass
import os

shortlist = ["mdisk.me", "droplink.co", "mdisk"]


# mdisk

def mdisk(url):
    api = "https://api.emilyx.in/api"
    client = cloudscraper.create_scraper(allow_brotli=False)
    resp = client.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    try:
        resp = client.post(api, json={"type": "mdisk", "url": url})
        res = resp.json()
    except BaseException:
        return "API UnResponsive / Invalid Link !"
    if res["success"] is True:
        return res["url"]
    else:
        return res["msg"]

# droplink

def droplink(url):
    api = "https://api.emilyx.in/api/bypass"
    client = cloudscraper.create_scraper(allow_brotli=False)
    resp = client.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    try:
        resp = client.post(api, json={"type": "droplink", "url": url})
        res = resp.json()
    except BaseException:
        return "API UnResponsive / Invalid Link !"
    if res["success"] is True:
        return res["url"]
    else:
        return res["msg"]


def mdis_k(urlx):
    scraper = cloudscraper.create_scraper(interpreter="nodejs", allow_brotli=False)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"
    }
    apix = f"http://x.egraph.workers.dev/?param={urlx}"
    response = scraper.get(apix, headers=headers)
    query = response.json()
    return query


def mdisk(url):
    check = re.findall(r"\bhttps?://.*mdisk\S+", url)
    if not check:
        textx = f"**Invalid link**"
        return textx
    else:
        try:
            fxl = url.split("/")
            urlx = fxl[-1]
            uhh = mdis_k(urlx)
            duration = {uhh["duration"]}
            text = f'**📂 Title** : `{uhh["filename"]}`\n\n📥 **Download URL (If mxv Present in link then it support only MX player\n\nIf dash, mpd, M3U8, hls present in link then it support all player)** :- {uhh["source"]}\n\n📤 **Download URL (Support Only MX Player)** :- {uhh["download"]}\n\n💎 **Uploader User ID** :- `{uhh["from"]}`\n\n💠 **Uploader User Name** :- `@{uhh["display_name"]}`\n\n📹 **Video Width** :- `{uhh["width"]}`\n\n🎞 **Video Height** :- {uhh["height"]}\n\n📦 **Video Duration** :- `{uhh["duration"]}s`\n\n📊 **Video Size** :- `{uhh["size"]}kb`'
            return text
        except ValueError:
            textx = f"The Content is Deleted."
            return textx


