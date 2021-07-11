from .. import Dipesh
from telethon import events, Button

DIPESH_USER = [1809900087]

@Dipesh.on(
    events.NewMessage(pattern="^/repo ?(.*)"))
async def _(event):
  if event.sender_id == DIPESH_USER:
    await Dipesh.send_message(HEY MASTER HERE IS YOUR REPO\n\n https://github.com/itzdipesh/DIPESH-PM-BOT)
  else:
    await event.reply("**BHAI YAAR THUM GAAND MARAO**")
