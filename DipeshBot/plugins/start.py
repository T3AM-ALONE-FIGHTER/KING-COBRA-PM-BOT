# By < @xditya >
# // @Dipesh //
from .. import Dipesh
from telethon import events, custom, Button
DIPESH_PIC = "https://telegra.ph/file/d4a838d9c89d0bbeb919e.jpg"
@Dipesh.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await Dipesh.send_file(event.chat_id,
                                  DIPESH_PIC,
                                  caption="ππππποΌ―  ππππ!!\nπΈπΌ πΏπ΄πππΎπ½π°π» π°πππΈπππ°π½π πΎπ΅ @BLACK_MAFIA_OWNER",
                                  buttons=[
                                      (Button.inline(
                                          "plugins >>",
                                          data="mhelp"))]
                                  )

@Dipesh.on(events.callbackquery.CallbackQuery(data="creator"))
async def creator(event):
    await event.edit(event.chat_id, "π·π΄ππ΄ πΈπ πΌπ πΌπ°πππ΄π πππ΄ππ½π°πΌπ΄  @BLACK_MAFIA_OWNER", show_alert=True)

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
    await event.edit("β’/sed to enter sed lyf.\nβ’/stop to leave sed lyf.\nβ’/alive to check bot is alive or not.\nβ’/repo to get source code of this bot.")
    
@Dipesh.on(events.callbackquery.CallbackQuery(data="mhelpk"))
async def oooooookk(event):
    await event.edit("BHAJ YAAR TUM GAND MARAO")
