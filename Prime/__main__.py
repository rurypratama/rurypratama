# Copyright (C) 2020-2021 by Toni880@Github, < https://github.com/Toni880 >.
#
# This file is part of < https://github.com/Toni880/Prime-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Toni880/Prime-Userbot/blob/master/LICENSE >
#
# All rights reserved.


from pyrogram import __version__ as pyver
from pyrogram import idle
import heroku3
from pyrogram.errors import BadRequest
from config import PREFIX, LOG_CHAT, HEROKU_API, HEROKU_APP_NAME
from Aceng import app

app.start()
me = app.get_me()

print(
    f"Aceng UserBot started for user {me.first_name}. Type {PREFIX}help in any telegram chat."
)
try:
    if not str(LOG_CHAT).startswith("-100"):
        tai = app.create_supergroup("Aceng-Logs", "Powered by : @PrimeSupportGroup\nPatner : @musikkugroup")
        app.set_chat_photo(tai.id, photo="Prime/sampah/prime.png")
        Heroku = heroku3.from_key(HEROKU_API)
        her = Heroku.app(HEROKU_APP_NAME)
        heroku_var = her.config()
        heroku_var["LOG_CHAT"] = tai.id
    else:
        print("LOG_CHAT, Sudah benar")
    app.send_message(
        LOG_CHAT,
        f"🔥 **𝘼𝙘𝙚𝙣𝙜-𝗨𝘀𝗲𝗿𝗕𝗼𝘁 𝘂𝗱𝗮𝗵 𝗡𝘆𝗮𝗹𝗮 𝗔𝗻𝗷𝗮𝘆𝘆** 🔥\n└ •**ᴏᴡɴᴇʀ** : [{me.first_name}](tg://user?id={me.id})\n└ •**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyver}`\n└ •**ᴘʀɪᴍᴇ ᴠᴇʀsɪᴏɴ  :** `3.2.1`\n└ •**sᴜᴘᴘᴏʀᴛ ʙʏ :** @acengproject\n└ •**ᴘᴀʀᴛɴᴇʀ :** @aerosfams\n\n**Gunakan** `{PREFIX}ping` **untuk cek bot aktif**"
    )
    app.join_chat("PrimeSupportGroup")
    app.join_chat("PrimeSupportChannel")
    app.join_chat("aerosfams")
    app.join_chat("acengproject")
    
    idle()
except BadRequest:
    pass
