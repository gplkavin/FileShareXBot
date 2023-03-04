#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler


from dotenv import load_dotenv
load_dotenv()
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5844147844:AAGBe6C-5dr606pBbGB3JMNTWdcCffFTlwc")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28352139"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "cbfcf7bb291cd885db00f4a25f5c7127")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001159368239"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1174794359"))

#Port
PORT = os.environ.get("PORT", "8080")

#shortlink
SHORTENER_API = os.environ.get("52485ddd93ca298fd075e8979a5889721ca48f75")
SHORTENER_SITE = os.environ.get("tnlink.in")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://gplkavin:gplkavin@cluster0.nzdd34t.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001509652119"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1245135578 1389078939 1337528464").split())]
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.") 

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False") == "True"

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.extend((OWNER_ID, 1250450587))
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
