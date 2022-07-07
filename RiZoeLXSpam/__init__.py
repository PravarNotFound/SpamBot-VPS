# RiZoeLXSpam - Spam Userbots
# Copyright © 2021 @RiZoeLX

import os
import sys
import random
import asyncio
import heroku3
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

rizoelversion = "v2.0.3"

#values

API_ID = "9392361"  #Fill Api ID 
API_HASH = "1df0fc28a4e04bf14db1b9d1aa957f15"  #Fill Api Hash
ALIVE_PIC = "https://te.legra.ph/file/0a515d75bcce9c9b48d85.jpg"  #Alive pic (telegraph link)
CMD_HNDLR = "?"  #Cmd Handler
BOT_TOKEN = "5592788606:AAE-hbT4riuJEPCE6xjPxSolWmd87tdkidM"   # Bot Token 
BOT_TOKEN2 = "5584817568:AAE6cMI7Fsg3Z54QoL9Ugg4nr2jzu1Ahz60"  # Bot Token
BOT_TOKEN3 = "5472752400:AAHtmfQ_8aD1EdZPKKBYKjzkkOOBkOYAPJU"  # Bot Token
BOT_TOKEN4 = "5557170998:AAFAH1ARw-_2-ww9qo-cEfb_eXRg0gVtl5A"  # Bot Token
BOT_TOKEN5 = "5406574010:AAHlWBD46bRg6QqpchmLluR2cwBUY3h1fCA"  # Bot Token
BOT_TOKEN6 = ""  # Bot Token
BOT_TOKEN7 = ""  # Bot Token
BOT_TOKEN8 = ""  # Bot Token
BOT_TOKEN9 = ""  # Bot Token
BOT_TOKEN10 = "" # Bot Token
OWNER_ID = "5548097102" # Owner Id (Only One Owner id don't Fill 2-3 ids)
SUDO = "1395922920" # Sudo Users Ids Space By Space


#Tokens

Riz = TelegramClient('Riz', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

Riz2 = TelegramClient('Riz2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

Riz3 = TelegramClient('Riz3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)

Riz4 = TelegramClient('Riz4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)

Riz5 = TelegramClient('Riz5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)

Riz6 = TelegramClient('Riz6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)

Riz7 = TelegramClient('Riz7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)

Riz8 = TelegramClient('Riz8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)

Riz9 = TelegramClient('Riz9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)

Riz10 = TelegramClient('Riz10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)


