import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6877855234:AAGN4L-oizvVVv9Lmub5YrbHHCqLPhP6a-Y")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24407770"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4f6840d55ecb0a4f49e79295a1847713")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002119358127"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1331434457"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://kanishkagarg:XY0rw2EtDwCrHTYi@cluster0.6cirkqm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1001932990033"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1001803674305"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b> Kᴏɴɴɪᴄʜɪᴡᴀ {first} 👋 </b>\n\nI ᴀᴍ ᴀ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ @The_bot_coder")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6717624918 6984236882 6056484807 6950166258 6530416380 2050015292").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "〒Hi! \nPlease Join our channel First then Download by tapping on ʀᴇʟᴏᴀᴅ  \nThank You✦")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "​🚫Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ​ - @Anime_Gallery_official"

ADMINS.append(OWNER_ID)
ADMINS.append(1331434457)

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
