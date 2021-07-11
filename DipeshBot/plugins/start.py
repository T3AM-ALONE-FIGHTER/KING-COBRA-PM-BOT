# By < @xditya >
# // @Dipesh //
from .. import Dipesh
from telethon import events, custom, Button
DIPESH_PIC = "https://telegra.ph/file/40bda831eb7241fe978d1.jpg"
@Dipesh.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await Dipesh.send_file(event.chat_id,
                                  DIPESH_PIC,
                                  caption="ＨＥＬＬＯ  ＶＭＲＯ!!\n𝙸𝙼 𝙿𝙴𝚁𝚂𝙾𝙽𝙰𝙻 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙾𝙵 @DIPESH_XD"
                                  buttons=[
                                      (Button.inline(
                                          "plugins >>",
                                          data="mhelp"))]
                                  )

@Dipesh.on(events.callbackquery.CallbackQuery(data="creator"))
async def creator(event):
    await event.edit(event.chat_id, "𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴  @DIPESH_XD", show_alert=True)

########################################################################################################################################


@Dipesh.on(events.callbackquery.CallbackQuery(data="mhelp"))
async def ommmmk(event):
    await event.edit("ʜᴇʟᴘ ᴍᴇɴᴜ",
                    buttons=[
                        [Button.inline("ᴍᴀsᴛᴇʀ ᴛᴏᴏʟs", data="ots")],
                        [Button.inline("ᴛᴏᴏʟs", data="mhelpk")]
                    ])
                     
@Dipesh.on(events.callbackquery.CallbackQuery(data="ots"))
async def oppppppppp(event):
    await event.edit("•/sed for sed lyf.\n•/stop to stop sed lyf.\n•/alive to check bot is alive or not.")
    
@Dipesh.on(events.callbackquery.CallbackQuery(data="mhelpk"))
async def oooooookk(event):
    await event.edit("ᴊᴏɪɴ @AboutDipesh")
