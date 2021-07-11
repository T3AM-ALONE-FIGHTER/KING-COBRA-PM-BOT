from .. import Dipesh
from telethon import events, Button

@Dipesh.on(events.NewMessage(incoming=True, pattern="/alive"))
async def alibe(event):
  DIPESH_PIC = "https://telegra.ph/file/40bda831eb7241fe978d1.jpg"
  but = [[Button.url("ᴏᴡɴᴇʀ", "t.me/DIPESH_XD")]]
  pm_caption = "•**ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴍʏ ᴍᴀsᴛᴇʀ**\n\n"
  pm_caption += "•**ᴍʏ sʏsᴛᴇᴍ ɪs ᴘᴇʀғᴇᴄᴛʟʏ ʀᴜɴɴɪɢ**\n\n"
  pm_caption += "• ᴀʙᴏᴜᴛ ᴍʏ sʏsᴛᴇᴍ ✗\n\n"
  pm_caption += "• 𝙎𝙈𝙀𝙓 𝙓 𝙑𝙀𝙍𝙎𝙄𝙊𝙉: 1.1\n"
  pm_caption += "• 𝙏𝙀𝙇𝙀𝙏𝙃𝙊𝙉 𝙑𝙀𝙍𝙎𝙄𝙊𝙉 ☞ {version.__version__}\n"
  pm_caption += (
        "• 𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔 ☞ [「ᴅɪᴘᴇsʜ」❤️🥀](t.me/DIPESH_XD)\n\n"
    )
  pm_caption += f"• 𝘾𝙍𝙀𝘼𝙏𝙊𝙍 ☞ [「ᴅɪᴘᴇsʜ」❤️🥀](t.me/DIPESH_XD)\n"
  await Dipesh.send_file(event. chat_id, file=BANG_PIC, captions=pm_caption, buttons=but, link_preview=False)
