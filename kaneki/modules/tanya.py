from kaneki.events import register
import random

APAKAH_STRINGS = (
    "iya",
    "tidak",
    "mungkin",
    "bisa jadi",
    "anda benar sekali",
    "anda salah besar",
    "👍",
    "👎",
)


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    kontol = event.pattern_match.group(1)
    if not kontol:
        return await event.reply("Example: /apakah (text)")
    else:
        return await event.reply(random.choice(APAKAH_STRINGS))
