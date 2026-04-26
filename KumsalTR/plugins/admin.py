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
    """Yanıtlanan .txt dosyasını veya metni çerez olarak yükler"""
    # Özel mesajda dosya veya metin gönderilirse de çalışsın
    is_reply = m.reply_to_message is not None
    target = m.reply_to_message if is_reply else m
    
    if target.document:
        doc = target.document
        if not doc.file_name or not doc.file_name.endswith(".txt"):
            return await m.reply_text("<b>❌ Dᴏsʏᴀ .ᴛxᴛ ғᴏʀᴍᴀᴛɪɴᴅᴀ ᴏʟᴍᴀʟɪᴅɪʀ.</b>")
        
        sent = await m.reply_text("<b>🔄 Çᴇʀᴇᴢ ᴅᴏsʏᴀsɪ ɪşʟᴇɴɪʏᴏʀ...</b>")
        try:
            os.makedirs(yt.cookie_dir, exist_ok=True)
            path = os.path.join(yt.cookie_dir, doc.file_name)
            await target.download(file_name=path)
            yt.normalize_cookie_file(path)
            yt.checked = False
            yt.cookies = []
            yt.get_cookies()
            count = len(yt.cookies)
            await sent.edit_text(f"<b>✅ Çᴇʀᴇᴢ ʙᴀşᴀʀɪʏʟᴀ ʏᴜ̈ᴋʟᴇɴᴅɪ!</b>\n\n📂 <code>{path}</code>\n📊 Tᴏᴘʟᴀᴍ ᴀᴋᴛɪғ ᴄ̧ᴇʀᴇᴢ: {count}")
        except Exception as e:
            logger.error(f"Cookie upload error: {e}")
            await sent.edit_text(f"<b>❌ Hᴀᴛᴀ: {e}</b>")
            
    elif target.text and (not is_reply or (is_reply and len(m.command) == 1)):
        # Eğer komutun yanında metin varsa veya metne yanıt verilmişse
        cookie_text = target.text if not is_reply else target.text
        if "youtube.com" not in cookie_text and "FALSE" not in cookie_text:
             if not is_reply: return await m.reply_text("<b>🍪 Lᴜ̈ᴛғᴇɴ ʙɪʀ .ᴛxᴛ ᴄ̧ᴇʀᴇᴢ (ᴄᴏᴏᴋɪᴇ) ᴅᴏsʏᴀsɪɴɪ ʏᴀɴɪᴛʟᴀʏᴀʀᴀᴋ <code>/cookie</code> ʏᴀᴢɪɴ ᴠᴇʏᴀ ᴄ̧ᴇʀᴇᴢ ᴍᴇᴛɴɪɴɪ ɢᴏ̈ɴᴅᴇʀɪɴ.</b>")
        
        sent = await m.reply_text("<b>🔄 Çᴇʀᴇᴢ ᴍᴇᴛɴɪ ɪşʟᴇɴɪʏᴏʀ...</b>")
        try:
            os.makedirs(yt.cookie_dir, exist_ok=True)
            import time
            path = os.path.join(yt.cookie_dir, f"cookie_{int(time.time())}.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(cookie_text)
            
            yt.normalize_cookie_file(path)
            yt.checked = False
            yt.cookies = []
            yt.get_cookies()
            count = len(yt.cookies)
            await sent.edit_text(f"<b>✅ Çᴇʀᴇᴢ ᴍᴇᴛɴɪ ʙᴀşᴀʀɪʏʟᴀ ʏᴜ̈ᴋʟᴇɴᴅɪ!</b>\n\n📂 <code>{path}</code>\n📊 Tᴏᴘʟᴀᴍ ᴀᴋᴛɪғ ᴄ̧ᴇʀᴇᴢ: {count}")
        except Exception as e:
            logger.error(f"Cookie text error: {e}")
            await sent.edit_text(f"<b>❌ Hᴀᴛᴀ: {e}</b>")
    else:
        await m.reply_text("<b>🍪 Lᴜ̈ᴛғᴇɴ ʙɪʀ .ᴛxᴛ ᴄ̧ᴇʀᴇᴢ (ᴄᴏᴏᴋɪᴇ) ᴅᴏsʏᴀsɪɴɪ ʏᴀɴɪᴛʟᴀʏᴀʀᴀᴋ <code>/cookie</code> ʏᴀᴢɪɴ ᴠᴇʏᴀ ᴄ̧ᴇʀᴇᴢ ᴍᴇᴛɴɪɴɪ ɢᴏ̈ɴᴅᴇʀɪɴ.</b>")


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

