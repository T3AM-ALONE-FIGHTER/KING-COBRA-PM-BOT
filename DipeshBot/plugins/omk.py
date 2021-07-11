from .. import Dipesh
from telethon import events

@Dipesh.on(events.NewMessage(pattern="/skip"))
async def oommkkj(event):
  await event.send(event.chat_id, "**BHAG BETICHOD**")
