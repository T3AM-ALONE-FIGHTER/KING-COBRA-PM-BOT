from .. import Dipesh
from telethon import events, Button

@Dipesh.on(events.NewMessage(incoming=True, pattern="/alive"))
async def alibe(event):
  DIPESH_PIC = "https://telegra.ph/file/40bda831eb7241fe978d1.jpg"
  but = [[Button.url("ᴏᴡɴᴇʀ", "t.me/DIPESH_XD")]]