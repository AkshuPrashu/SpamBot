import asyncio

from .. import Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, SUDO_USERS import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon import events
import os
import random
import sys
    

@Riz.on(events.NewMessage(pattern=r"\.bleave"))
@Riz2.on(events.NewMessage(pattern=r"\.bleave"))
@Riz3.on(events.NewMessage(pattern=r"\.bleave"))
@Riz4.on(events.NewMessage(pattern=r"\.bleave"))
@Riz5.on(events.NewMessage(pattern=r"\.bleave"))
@Riz6.on(events.NewMessage(pattern=r"\.bleave"))
@Riz7.on(events.NewMessage(pattern=r"\.bleave"))
@Riz8.on(events.NewMessage(pattern=r"\.bleave"))
@Riz9.on(events.NewMessage(pattern=r"\.bleave"))
@Riz10.on(events.NewMessage(pattern=r"\.bleave"))
@Riz11.on(events.NewMessage(pattern=r"\.bleave"))
@Riz12.on(events.NewMessage(pattern=r"\.bleave"))
@Riz13.on(events.NewMessage(pattern=r"\.bleave"))
@Riz14.on(events.NewMessage(pattern=r"\.bleave"))
@Riz15.on(events.NewMessage(pattern=r"\.bleave"))
@Riz16.on(events.NewMessage(pattern=r"\.bleave"))
@Riz17.on(events.NewMessage(pattern=r"\.bleave"))
@Riz18.on(events.NewMessage(pattern=r"\.bleave"))
@Riz19.on(events.NewMessage(pattern=r"\.bleave"))
@Riz20.on(events.NewMessage(pattern=r"\.bleave"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SUDO_USERS:
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = rizoel[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )   
