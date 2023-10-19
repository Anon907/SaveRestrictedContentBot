#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("24082128", default=None, cast=int)
API_HASH = config(dfac987a12a41d1075e691d94f9d4802"", default=None)
BOT_TOKEN = config("6628752841:AAE_i6jYHgn7abCScGC1jEMtXum77AuHMzI", default=None)
SESSION = config("1BVtsOLIBu6zMceJCB7U2Uqzs08bGtelJpGc1ETqh_co4whzX3Cl7KDTmgIC8jxx92jCWpNPW5tLGEKmbxQC5n3sU1rGD29hEjC4bhxRcK8bcGN4_4vlSoy_fUXhIsrGXntGDfeW4YMIX9gmtO4BLO73tP9Z0XSjPgikCLDERO8n1zf3kQZNxPiMuvp5pXGnu5CPtP9nd1F5RadjKs90bFWoj8P987-rwC8gyTDjXqTWZsyIq3ewKwrG6fjlKR0mw8pfDEgbig8a85kWQocpBX_zQFW74WNgdPmhV7BDD5Xhf7A3aPeFgB2ZnC93x_WcLncYDVhnZ2ETTi-yEW2v_zJhJOtXb6Z4=", default=None)
FORCESUB = config("ZikaStore907", default=None)
AUTH = config("1914436153", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
