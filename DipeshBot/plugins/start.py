# By < @xditya >
# // @Dipesh //
from .. import Dipesh
from telethon import events, custom, Button
DIPESH_PIC = "https://telegra.ph/file/d4a838d9c89d0bbeb919e.jpg"
@Dipesh.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await Dipesh.send_file(event.chat_id,
                                  DIPESH_PIC,
                                  caption="𝐇𝐄𝐋𝐋𝐎Ｏ  𝐁𝐄𝐓𝐀!!\n𝙸𝙼 𝙿𝙴𝚁𝚂𝙾𝙽𝙰𝙻 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙾𝙵 @BLACK_MAFIA_OWNER",
                                  buttons=[
                                      (Button.inline(
                                          "plugins >>",
                                          data="mhelp"))]
                                  )

@Dipesh.on(events.callbackquery.CallbackQuery(data="creator"))
async def creator(event):
    await event.edit(event.chat_id, "𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴  @BLACK_MAFIA_OWNER", show_alert=True)

########################################################################################################################################


@Dipesh.on(events.callbackquery.CallbackQuery(data="mhelp"))
async def ommmmk(event):
    await event.edit("HELP MENU",
                    buttons=[
                        [Button.inline("Master tool >>", data="ots")],
                        [Button.inline("tools", data="mhelpk")]
                    ])
                     
@Dipesh.on(events.callbackquery.CallbackQuery(data="ots"))
async def oppppppppp(event):
    await event.edit("•/sed to enter sed lyf.\n•/stop to leave sed lyf.\n•/alive to check bot is alive or not.\n•/repo to get source code of this bot.")
    
@Dipesh.on(events.callbackquery.CallbackQuery(data="mhelpk"))
async def oooooookk(event):
    await event.edit("BHAJ YAAR TUM GAND MARAO")
