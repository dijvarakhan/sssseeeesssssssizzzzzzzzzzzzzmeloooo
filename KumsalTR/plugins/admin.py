# @The_Team_kumsal tarafından yasal olarak geliştirildi keyifli kullanımlar #kumsalteam

import os
from pyrogram import filters, types
from KumsalTR import app, yt, config, lang, logger


@app.on_message(filters.command(["cookies", "cerezler"]) & app.sudo_filter)
@lang.language()
async def cookies_status(_, m: types.Message):
    """Cookie havuzunun durumunu gösterir"""
    yt.checked = False
    yt.get_cookies()
    
    cookie_count = len(yt.cookies)
    cookie_dir = yt.cookie_dir
    
    text = f"<b>🍪 Çᴇʀᴇᴢ Dᴜʀᴜᴍᴜ</b>\n\n"
    text += f"<b>📂 Dɪᴢɪɴ:</b> <code>{cookie_dir}</code>\n"
    text += f"<b>📊 Aᴋᴛɪғ Çᴇʀᴇᴢ:</b> {cookie_count}\n\n"
    
    if yt.cookies:
        for i, c in enumerate(yt.cookies, 1):
            name = os.path.basename(c)
            size = os.path.getsize(c) if os.path.exists(c) else 0
            text += f"  {i}. <code>{name}</code> ({size} byte)\n"
    else:
        text += "<i>Hᴇɴᴜ̈ᴢ ʜɪᴄ̧ ᴄ̧ᴇʀᴇᴢ ʏᴜ̈ᴋʟᴇɴᴍᴇᴍɪş.</i>\n"
    
    text += f"\n<b>Kᴏᴍᴜᴛʟᴀʀ:</b>\n"
    text += f"• <code>/cookie</code> — .ᴛxᴛ ᴅᴏsʏᴀ ʏᴀɴɪᴛʟᴀʏᴀʀᴀᴋ ʏᴜ̈ᴋʟᴇ\n"
    text += f"• <code>/cookietemizle</code> — Tᴜ̈ᴍ ᴄ̧ᴇʀᴇᴢʟᴇʀɪ sɪʟ"
    
    await m.reply_text(text)


@app.on_message(filters.command(["cookie", "cerezkoy"]) & app.sudo_filter)
@lang.language()
async def update_cookie(_, m: types.Message):
    """Yanıtlanan veya açıklamasında /cookie yazan .txt dosyasını çerez olarak yükler"""
    reply = m.reply_to_message
    if reply and reply.document:
        target = reply
    elif m.document:
        target = m
    else:
        return await m.reply_text("<b>🍪 Lᴜ̈ᴛғᴇɴ ʙɪʀ .ᴛxᴛ ᴄ̧ᴇʀᴇᴢ (ᴄᴏᴏᴋɪᴇ) ᴅᴏsʏᴀsɪɴɪ ʏᴀɴɪᴛʟᴀʏᴀʀᴀᴋ ᴠᴇʏᴀ ᴅᴏsʏᴀ ᴀᴄ̧ɪᴋʟᴀᴍᴀsɪɴᴀ ʏᴀᴢᴀʀᴀᴋ <code>/cookie</code> ʏᴀᴢɪɴ.</b>")
    
    doc = target.document
    if not doc.file_name or not doc.file_name.endswith(".txt"):
        return await m.reply_text("<b>❌ Dᴏsʏᴀ .ᴛxᴛ ғᴏʀᴍᴀᴛɪɴᴅᴀ ᴏʟᴍᴀʟɪᴅɪʀ.</b>")
    
    sent = await m.reply_text("<b>🔄 Çᴇʀᴇᴢʟᴇʀ ɪşʟᴇɴɪʏᴏʀ...</b>")
    
    try:
        os.makedirs(yt.cookie_dir, exist_ok=True)
        path = os.path.join(yt.cookie_dir, doc.file_name)
        
        # Eğer dosya varsa sil ki temiz indirme olsun
        if os.path.exists(path):
            os.remove(path)
            
        await target.download(file_name=path)
        
        if not os.path.exists(path):
            return await sent.edit_text("<b>❌ Dᴏsʏᴀ ɪɴᴅɪʀɪʟᴇᴍᴇᴅɪ.</b>")

        # Formatı düzelt
        yt.normalize_cookie_file(path)
        
        # YouTube core'u tetikle
        yt.checked = False
        yt.cookies = []
        yt.get_cookies()
        
        count = len(yt.cookies)
        await sent.edit_text(f"<b>✅ Çᴇʀᴇᴢ ʙᴀşᴀʀɪʏʟᴀ ʏᴜ̈ᴋʟᴇɴᴅɪ!</b>\n\n📂 <code>{path}</code>\n📊 Tᴏᴘʟᴀᴍ ᴀᴋᴛɪғ ᴄ̧ᴇʀᴇᴢ: {count}")
        logger.info(f"New cookie uploaded: {path} (Total: {count})")
    except Exception as e:
        logger.error(f"Cookie upload error: {e}")
        await sent.edit_text(f"<b>❌ Hᴀᴛᴀ: {e}</b>")


@app.on_message(filters.command(["cookietemizle", "clearcookies"]) & app.sudo_filter)
@lang.language()
async def clear_cookies(_, m: types.Message):
    """Tüm çerezleri siler"""
    count = 0
    if os.path.exists(yt.cookie_dir):
        for f in os.listdir(yt.cookie_dir):
            if f.endswith(".txt"):
                try:
                    os.remove(os.path.join(yt.cookie_dir, f))
                    count += 1
                except:
                    pass
    
    yt.checked = False
    yt.cookies = []

    await m.reply_text(f"<b>🧹 {count} ᴀᴅᴇᴛ ᴄ̧ᴇʀᴇᴢ ᴅᴏsʏᴀsɪ ᴛᴇᴍɪᴢʟᴇɴᴅɪ.</b>")


@app.on_message(filters.command(["clearcache"]) & app.sudo_filter)
async def clear_cache_cmd(_, m: types.Message):
    count = 0
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    for file in os.listdir("downloads"):
        try:
            os.remove(f"downloads/{file}")
            count += 1
        except:
            continue
    await m.reply_text(f"<b>🧹 {count} ᴀᴅᴇᴛ ᴏ̈ɴʙᴇʟʟᴇᴋ ᴅᴏsʏᴀsɪ ᴛᴇᴍɪᴢʟᴇɴᴅɪ.</b>")
@app.on_message(filters.command("id"))
async def id_check(_, m: types.Message):
    """Kullanıcı ve sohbet ID'sini gösterir, sudo durumunu belirtir"""
    is_sudo = m.from_user.id in app.sudoers if m.from_user else False
    text = f"<b>👤 Kᴜʟʟᴀɴɪᴄɪ:</b> <code>{m.from_user.id if m.from_user else 'Bilinmiyor'}</code>\n"
    text += f"<b>👥 Sᴏʜʙᴇᴛ:</b> <code>{m.chat.id}</code>\n"
    text += f"<b>🛡️ Sᴜᴅᴏ:</b> {'✅ Evet' if is_sudo else '❌ Hayır'}"
    await m.reply_text(text)

