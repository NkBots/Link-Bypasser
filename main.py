import pyrogram
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import os
import requests
import threading 
import re
import cloudscraper

# bot
bot_token = os.environ.get("TOKEN", "")
api_hash = os.environ.get("HASH", "") 
api_id = os.environ.get("ID", "")
app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)  




@app.on_message(filters.command('mdisk'))
async def link_handler(bot, message):
 # link = message.matches[0].group(0)
  l = message.text.split(' ', 1)

  if len(l) == 1:
        return await message.reply_text('Send Me Any Mdisk Link Like this `/mdisk mdisk-link`')
  link = l[1]
  #mess = await message.reply_text("**Bypassing...⏳**",quote=True)

  if 'mdisk' in link:
     try:
        mess = await message.reply_text("**Bypassing...⏳**",quote=True)
        short_link = mdisk(link)
        await mess.edit_text(f"**Bypassed URL** : {short_link} \n\n © {message.from_user.mention}", disable_web_page_preview=True)
     except Exception as e:
        await mess.edit_text(f"**Error** : {e}")



@app.on_message(filters.command('bypass'))
async def link_handler(bot, message):
 # link = message.matches[0].group(0)
  l = message.text.split(' ', 1)

  if len(l) == 1:
        return await message.reply_text('Send Me Any Link Like this `/bypass link`')
  link = l[1]
  #mess = await message.reply_text("**Bypassing...⏳**",quote=True)

  if '' in link:
     try:
        mess = await message.reply_text("**Bypassing...⏳**",quote=True)
        short_link = (link)
        await mess.edit_text(f"**Bypassed URL** : {short_link} \n\n © {message.from_user.mention}", disable_web_page_preview=True)
     except Exception as e:
        await mess.edit_text(f"**Error** : {e}")






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


url = "" #@param {type:"string"}
# ==============================================

def droplink(url):
    api = "https://api.emilyx.in/api"
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

# ==============================================

res = droplink(url)

print(res)












# server loop
print("Bot Starting")
app.run()
