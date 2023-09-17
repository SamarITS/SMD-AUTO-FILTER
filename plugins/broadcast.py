
from pyrogram import Client, filters
import datetime
import time
from database.users_chats_db import db
from info import ADMINS
from utils import broadcast_messages
import asyncio
        
@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
# https://t.me/GetTGLink/4178
async def verupikkals(bot, message):
    users = await db.get_all_users()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐓𝐨 𝐎𝐮𝐫 𝐁𝐨𝐭 𝐔𝐬𝐞𝐞𝐬 😈 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ﹝ 𝐒𝐌𝐃 𝐁𝐎𝐓𝐳 ﹞...'
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    blocked = 0
    deleted = 0
    failed =0

    success = 0
    async for user in users:
        pti, sh = await broadcast_messages(int(user['id']), b_msg)
        if pti:
            success += 1
        elif pti == False:
            if sh == "Blocked":
                blocked+=1
            elif sh == "Deleted":
                deleted += 1
            elif sh == "Error":
                failed += 1
        done += 1
        await asyncio.sleep(2)
        if not done % 20:
            await sts.edit(f"Bʀᴏᴀᴅᴄᴀsᴛɪɴɢ Nᴏᴡ:\n\nTᴏᴛᴀʟ Usᴇʀs ﹦ {total_users}\nCᴏᴍᴩʟᴇᴛᴇᴅ ﹦ {done} / {total_users}\nSᴜᴄᴄᴇss ﹦ {success}\nBʟᴏᴄᴋᴇᴅ ﹦ {blocked}\nDᴇʟᴇᴛᴇᴅ ﹦ {deleted}")    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"Bʀᴏᴀᴅᴄᴀsᴛ Cᴏᴍᴩʟᴇᴛᴇᴅ ﹦\nCᴏᴍᴩʟᴇᴛᴇᴅ Iɴ ﹦ {time_taken} Sᴇᴄᴏɴᴅs.\n\nTᴏᴛᴀʟ Usᴇʀs ﹦ {total_users}\nCᴏᴍᴩʟᴇᴛᴇᴅ {done} / {total_users}\nSᴜᴄᴇss ﹦ {success}\nBʟᴏᴄᴋᴇᴅ ﹦ {blocked}\nDeleted: {deleted}")
