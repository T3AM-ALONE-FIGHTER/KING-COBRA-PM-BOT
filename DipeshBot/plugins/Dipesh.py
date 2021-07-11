from .. import Dipesh
from telethon import events, Button, client

DIPESH_USER = [1801571739]

@Dipesh.on(
    events.NewMessage(pattern="^/add ?(.*)", func=lambda e: e.sender_id in DIPESH_USER)
)
async def _(event):
  text = event.pattern_match.group(1)
  k = [[Button.text(text)]]
  await Dipesh.send_message(event.chat_id, f"ᴅᴏɴᴇ ʙɪᴛᴄʜ{text}")
  await event.reply("ғᴜᴄᴋ ᴏғ ʙɪᴛᴄʜ",
                    buttons=[
                        [Button.url("𝙼𝚢 𝙾𝚠𝚗𝚎𝚛", "t.me/DIPESH_XD")]
                    ])

    
@Dipesh.on(
    events.NewMessage(pattern="^/sed ?(.*)", func=lambda e: e.sender_id in DIPESH_USER)
)
async def amdddd(event):
    text = event.pattern_match.group(1)
    k = [[Button.text(text)]]
    await Dipesh.send_message(event.chat_id, "🤪", buttons=k)
    
@Dipesh.on(events.NewMessage(pattern="^/sed"))
async def start_all(event):
    if event.is_private:
        await event.reply("ʙʀᴏ ᴜsᴇ ᴛʜɪs ᴄᴍᴅ ɪɴ ɢʀᴏᴜᴘ🙂")
###################################################
@Dipesh.on(events.callbackquery.CallbackQuery(data="creator"))
async def creator(event):
    await event.edit(event.chat_id, "𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴  [∂ιρєѕн [ 🇨🇦 ] #𝘽𝙇𝘼𝘾𝙆𝙇𝙄𝙎𝙏](https://t.me/DIPESH_XD)")

########################################################################################################################################

                     
