from pyrogram import filters
from pyrogram.types import  Message
from pyrogram.types import InputMediaPhoto
from .. import pbot as  Mukesh,BOT_USERNAME
import requests

# @Mukesh.on_message(filters.command("imagine"))
# async def imagine_(b, message: Message):
#     if message.reply_to_message:
#         text = message.reply_to_message.text
#     else:

#         text =message.text.split(None, 1)[1]
#     m =await message.reply_text( "`Please wait...,\n\nGenerating prompt .. ...`")
    
#     params = {
#     'query': text}
#     results = requests.post(url, headers=headers, params=params).json()["results"]

#     caption = f"""
# sᴜᴄᴇssғᴜʟʟʏ Gᴇɴᴇʀᴀᴛᴇᴅ 💘
# ✨ **Gᴇɴᴇʀᴀᴛᴇᴅ ʙʏ :** @{BOT_USERNAME}
# 🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
# """
#     await m.delete()
#     photos=[]
#     for i in range(5):
#         photos.append(InputMediaPhoto(results[i]))
#     photos.append(InputMediaPhoto(results[5], caption=caption))
#     await b.send_media_group(message.chat.id, media=photos)
    
# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
# __mod_name__ = "Aɪ ɪᴍᴀɢᴇ"
# __help__ = """
#  ➻ /imagine : ɢᴇɴᴇʀᴀᴛᴇ Aɪ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴛᴇxᴛ
#  ➻ /mahadev : ɢᴇɴᴇʀᴀᴛᴇ Mᴀʜᴀᴅᴇᴠ ɪᴍᴀɢᴇ
#  """
