import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "29189457")) #optional
API_HASH = getenv("API_HASH", "299fed7c8e58bc6f9a596c0d53675757") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8187361583 1281282633").split()))
OWNER_ID = int(getenv("OWNER_ID", "5305991541"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://ftyvfbgubhu7:hDZwwlNzlKBzls84@ameliamusicbot.f7dzw.mongodb.net/?retryWrites=true&w=majority&appName=AmeliaMusicbot")
BOT_TOKEN = getenv("BOT_TOKEN", "8168558389:AAEAtGW68o1kgjn1qAd1_o5VfnNRJoLRpao")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://graph.org/file/9ee37cccd7bf55c3ec953.png')
ALIVE_TEXT = getenv("ALIVE_TEXT", "ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙᴇ..🏓 \n\n\n ᴘᴏᴡᴇʀᴇᴅ ʙʏ ❤️ \n[𝅗ـﮩ٨ـ𝅽𝅾𓆩𝐇𖽞𖽖֯֟፝͢͡𖽸𖾓𝂬𓏲ࣹ᷼𝄢𝂬𝐁𖽞֟֠֯፝͢͡𖽖𖾓𓆪ﮩ٨ـ𝅽𝅾‐𝅘▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ](https://t.me/HeartBeat_Muzic)")
PM_LOGGER = getenv("PM_LOGGER", "-1002638782376")
LOG_GROUP = getenv("LOG_GROUP", "-1002588523310")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://t.me/HeartBeat_Muzic")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQG9ZVEAPkWaAczxnQL1GYiCT0ET6sP5is1h7jxA9NpLV9KQpmV-ut3X4xesbabksEmvnCyasatcmhmEhF1puTGAfcEVZzUqXAG4K1UsYspTii00YdY26x4ZaDZDDHLCp4jgruzUFca5c-HHQJ6690ekGpiYe3wF3CAwjWulpRHTENbKiBG0X8X2gHxaDz7iZkmt_GA8_DOQOUKGaZ9EISJO3yXKGj140c-TpUwL51MNAY_AKbu9ACfjCHP3hWsRvf_9wPD9lC-hqzc5gnPhT1SDafsFsknKt8U0-k2WzQ3LI23Xg2u0nr9J5Y7-5xrOcd1j5A7hOSAJjp3_GXGvBmUV11XVKwAAAAE8QwF1AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
