import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "7074117011:AAHeKuI6znMy4d-HcyEBOsJ-IkgHNUe47fo")

API_ID = int(os.environ.get("API_ID", "21661450"))

API_HASH = os.environ.get("API_HASH", "79612bc71908f95372808520a7eeee74")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
