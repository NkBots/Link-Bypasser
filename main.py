import pyrogram
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import os
import requests
import threading 


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
        short_link = await mdisk(link)
        await mess.edit_text(f"**Bypassed URL** : {short_link} \n\n © {message.from_user.mention}", disable_web_page_preview=True)
     except Exception as e:
        await mess.edit_text(f"**Error** : {e}")




# server loop
print("Bot Starting")
app.run()
