import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import Riz, Riz2, Riz3, Riz4, Riz5, Riz6, Riz7, Riz8, Riz9, Riz10, ALIVE_PIC

RIZ_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/0a8cec1011596c33154d8.jpg"


Riz_Button = [
        [
        Button.url("ᴏᴡɴᴇʀ", "https://t.me/TG_GoDfaTHeR")
        ]
        ]


@Riz.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! This is Private Userbot Of Team MLO**"
       await Riz.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)
                
@Riz2.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz2.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! This is Private Userbot Of Team MLO**"
       await Riz2.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)      
 
@Riz3.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz3.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! This is Private Userbot Of Team MLO**"
       await Riz3.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)
                
@Riz4.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz4.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! This is Private Userbot Of Team MLO**"
       await Riz4.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)  

@Riz5.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz5.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! This is Private Userbot Of Team MLO**"
       await Riz5.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)

@Riz6.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz6.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! This is Private Userbot Of Team MLO**"
       await Riz6.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)       

@Riz7.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz7.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id 
       firstname = replied_user.user.first_name
       Rizmsg = f"***Hello, {firstname} ! This is Private Userbot Of Team MLO**"
       await Riz7.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)

@Riz8.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz8.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! This is Private Userbot Of Team MLO**"
       await Riz8.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)
                
@Riz9.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz9.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! This is Private Userbot Of Team MLO**"
       await Riz9.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)
                
@Riz10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz10.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! This is Private Userbot Of Team MLO**"
       await Riz10.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)                
