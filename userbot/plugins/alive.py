from userbot import *
from userbot.utils import *
from userbot.cmdhelp import CmdHelp
from userbot.uniborgConfig import Config
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "BLACK GHOULS UserBot User"

PM_IMG = Config.ALIVE_PIC

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "True"

kraken = bot.uid

pm_caption = "__**ð¥ð¥GHOULS ÏÑÑÑÐ²ÏÑ Î¹Ñ ÏÎ· ÆÎ¹ÑÑð¥ð¥**__\n\n"

pm_caption += (
    f"               __â¼ð¼ð°ððð´ðâ__\n**ã[{DEFAULTUSER}](tg://user?id={kraken})ã**\n\n"
)

pm_caption += "â ÃªlÃªâ hÃ°Ã± VÃªrÂ§Ã¯Ã°Ã±: `1.15.0` \n"

pm_caption += "ê£ê¦êê»ê²ê ê¦êêªêêê²ê:      `3.7.4` \n"

pm_caption += f"ÄÉVÅâ± à¸¿Ãâ® VÉâ±¤â´ÅÃâ¦:  __**D.0**__\n"

pm_caption += f"sá´á´á´            : `{sudou}`\n"

pm_caption += "êê¤ê£ê£ê²êªê êêªê²ê¤ê£  : [á´á´ÉªÉ´](GHOULS MA AJA)\n"

pm_caption += "ð²ðððððð    : [KING COBRA OP]()\n\n"

pm_caption += "    [â¨REPOâ¨](https://telegra.ph/file/d66780ea8f868d037cc9a.jpg) ð¹ [ðLicenseð](https://github.com/KING-USER1/BLACK-GHOULS-BOT/blob/master/LICENSE)"



@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()

CmdHelp("alive").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'devil', None, 'Check weather yhe bit is alive or not. In your custom Alive Pic and Alive Msg if in Heroku Vars'
).add()
