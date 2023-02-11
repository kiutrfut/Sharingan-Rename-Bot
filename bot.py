import pyrogram
from pyrogram import Client
from pyrogram import filters
from pyrogram import enums
from pyrogram import idle
import logging
import config
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
import os

if bool(os.environ.get("WEBHOOK", False)):
    from config import Config
else:
    from config import Config

import pyrogram

# env
bot_token = os.environ.get("TOKEN", "5562112612:AAH7Sbz2iIAdoPknjv0FnuiNbiDa_5OFYQA") 
api_hash = os.environ.get("HASH", "8a50db8b70f8cbcbc013f013b6a58ac7") 
api_id = os.environ.get("ID", "22931292")

# bot
app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token, in_memory=True)



if __name__ == "__main__" :
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "RenameBot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )

app.run()
