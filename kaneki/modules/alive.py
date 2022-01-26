from telethon import Button

from kaneki import telethn as tbot
from kaneki.events import register

PHOTO = "https://telegra.ph/file/78729768e4dd0e38539ba.jpg"


@register(pattern=("/alive|/ALIVE"))
async def awake(event):
    event.sender.first_name
    KANEKI = "**Hello im ENVYCTION** \n\n"
    KANEKI += "**ALL SYSTEM WORKING PROPERLY**\n\n"
    KANEKI += " ☬ ⌊ **Python :** __3.9.7__ ⌉\n\n"
    KANEKI += " ☬ ⌊ **Pyrogram :** __1.2.9__ ⌉\n\n"
    KANEKI += " ☬ ⌊ **MongoDB :** __2.5.1__ ⌉\n\n"
    KANEKI += " ☬ ⌊ **Platform :** __linux__ ⌉\n\n"
    KANEKI += " ☬ ⌊ **My Lord** : [Artezid](https://t.me/{IDZ}) ☠⌉\n\n"
    KANEKI += " ☬ ⌊ **Envyction** ⌉\n\n"
    KANEKI += " ☬ ⌊ **TELETHON : 6.6.6 Latest** ⌉\n\n"
    KANEKI += " |||| || ||| |||| || |||||| ||||| || || ||"
    BUTTON = [
        [
            Button.url("Support", "https://t.me/TebBotSupport"),
            Button.url("Owner", "https://t.me/Cyberhunt"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=KANEKI, buttons=BUTTON)


__mod_name__ = "Alive"
