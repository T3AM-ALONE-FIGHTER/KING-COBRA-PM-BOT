# By < @xditya >
# // @Dipesh //
from .. import Dipesh
from telethon import events, custom, Button
DIPESH_PIC = "https://telegra.ph/file/3979593187378b2b54057.jpg"
@Dipesh.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await Dipesh.send_file(event.chat_id,
                                  SMEX_PIC,
                                  caption="ＨＥＬＬＯ  ＶＭＲＯ!!\n𝙸𝙼 𝙿𝙴𝚁𝚂𝙾𝙽𝙰𝙻 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙾𝙵 [∂ιρєѕн [ 🇨🇦 ] #𝘽𝙇𝘼𝘾𝙆𝙇𝙄𝙎𝙏](https://t.me/DIPESH_XD)")
                                  buttons=[
                                      (Button.inline(
                                          "ᴘʟᴜɢɪɴs",
                                          data="mhelp"))]
                                  )

@Dipesh.on(events.callbackquery.CallbackQuery(data="creator"))
async def creator(event):
    await event.edit(event.chat_id, "𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴  [∂ιρєѕн [ 🇨🇦 ] #𝘽𝙇𝘼𝘾𝙆𝙇𝙄𝙎𝙏](https://t.me/DIPESH_XD)", show_alert=True)

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
    await event.edit("ᴊᴏɪɴ [ᴀʙᴏᴜᴛᴅɪᴘᴇsʜ](https://t.meAboutDipesh)")
