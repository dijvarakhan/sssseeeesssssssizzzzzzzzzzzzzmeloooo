# @The_Team_kumsal tarafından yasal olarak geliştirildi keyifli kullanımlar #kumsalteam
import os
from pyrogram import filters, types
from KumsalTR import app, lang, yt, logger

@app.on_message(filters.command(["cookie", "cerez"]) & filters.private & ~app.blacklist_filter)
@lang.language()
async def cookie_cmd_hndlr(_, m: types.Message):
    if m.from_user.id not in app.sudoers:
        return

    # 1. Dosya Yanıtlama Kontrolü
    if m.reply_to_message and m.reply_to_message.document:
        if not m.reply_to_message.document.file_name.endswith(".txt"):
            return await m.reply_text("❌ **Lütfen geçerli bir .txt formatında cookie dosyası gönderin.**")
        
        sent = await m.reply_text("⏳ **Cookie dosyası indiriliyor ve işleniyor...**")
        path = await m.reply_to_message.download(file_name="KumsalTR/cookies/manual_cookie.txt")
        
        if yt.normalize_cookie_file(path):
            yt.checked = False # Yeniden yüklemeyi tetikle
            yt.get_cookies()
            await sent.edit_text(f"✅ **Cookie başarıyla güncellendi!**\n\n📂 Dosya: `{os.path.basename(path)}`")
        else:
            if os.path.exists(path): os.remove(path)
            await sent.edit_text("❌ **Cookie dosyası işlenirken hata oluştu. Formatı kontrol edin.**")
        return

    # 2. Metin Olarak Ekleme
    if len(m.command) > 1:
        content = m.text.split(None, 1)[1]
        path = os.path.join(yt.cookie_dir, f"text_cookie_{m.id}.txt")
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        
        if yt.normalize_cookie_file(path):
            yt.checked = False
            yt.get_cookies()
            await m.reply_text("✅ **Metin olarak gönderilen çerezler başarıyla kaydedildi ve aktif edildi!**")
        else:
            if os.path.exists(path): os.remove(path)
            await m.reply_text("❌ **Geçersiz çerez formatı.**")
        return

    # 3. Bilgi Gösterimi
    cookies = yt.get_cookies()
    text = f"🍪 **Mevcut Cookie Durumu:**\n\n"
    text += f"• **Aktif Dosya Sayısı:** `{len(cookies)}`\n"
    text += f"• **Klasör:** `KumsalTR/cookies/`\n\n"
    text += "💡 **Yeni cookie eklemek için:**\n"
    text += "1. Bir `.txt` dosyası gönderip bu komutu yanıt olarak kullanın.\n"
    text += "2. `/cookie [çerez metni]` şeklinde yazın."
    
    await m.reply_text(text)
