# @The_Team_kumsal tarafından yasal olarak geliştirildi keyifli kullanımlar #kumsalteam
# Copyright (c) 2025 TheHamkerAlone
# Licensed under the MIT License.
# This file is part of KumsalTR

from pyrogram import filters, types
from KumsalTR import app, lang, anon, db
from KumsalTR.helpers import buttons, Track, Utilities

utils = Utilities()

STATIONS = {
    "alem": ("ALEM FM", "https://turkmedya.radyotvonline.net/alemfmaac"),
    "joy": ("JOY FM", "https://carnival.live-streams.nl/joyfm.mp3"),
    "genc": ("GENÇ FM", "https://gencfmaac.radyotvonline.net/gencfm"),
    "r7": ("RADYO 7", "http://r7.radyotvonline.net:80/"),
    "pturk": ("POWER TÜRK", "http://power-turk.live-streams.nl/powerturk.mp3"),
    "plove": ("POWER LOVE", "http://power-love.live-streams.nl/powerlove.mp3"),
    "slow": ("SLOW TÜRK", "https://radyo.dogannet.tv/slowturk"),
    "kral": ("KRAL FM", "http://kralwmp.radyotvonline.com:80/"),
    "kpop": ("POWER K-POP", "http://powerapp.live-streams.nl/powerkpop.mp3"),
    "n1": ("NUMBER 1", "https://n10101m.mediacdn.com/numberone/live/playlist.m3u8"),
    "n1turk": ("NUMBER 1 TÜRK", "https://n10101m.mediacdn.com/numberoneturk/live/playlist.m3u8"),
    "baba": ("BABA RADYO", "http://46.20.7.126:80/"),
    "radyod": ("RADYO D", "https://radyo.dogannet.tv/radyod"),
    "seymen": ("RADYO SEYMEN", "http://radyoseymen.kesintisizyayin.com:8022/"),
    "super": ("SÜPER FM", "http://sc.superfm.com.tr:80/"),
    "virgin": ("VIRGIN RADIO", "http://virgin.live-streams.nl/virgin.mp3"),
    "sesiniz": ("VATAN FM", "http://yayin.vatanfm.com.tr:8050/"),
    "45lik": ("RADYO 45'LİK", "http://45lik.live-streams.nl/45lik.mp3"),
    "90s": ("POWER 90's", "http://powerapp.live-streams.nl/power90s.mp3"),
    "aturka": ("POWER TÜRK FM", "http://powerapp.live-streams.nl/powerturkfm.mp3"),
    "ask": ("AŞK FM", "http://askfm.kesintisizyayin.com:9244/"),
    "vturka": ("POWER POP", "http://powerapp.live-streams.nl/powerpop.mp3"),
    "romantik": ("ROMANTİK SES", "http://yayin.romantikses.com:8008/"),
    "metro": ("METRO FM", "http://sc.metrofm.com.tr:80/"),
    "fenomen": ("RADYO FENOMEN", "https://fenomen.listenfenomen.com/fenomen/128/icecast.audio"),
    "arabesk": ("POWER ARABESK", "http://powerapp.live-streams.nl/powerarabesk.mp3"),
    "efkar": ("POWER EFKAR", "http://powerapp.live-streams.nl/powerefkar.mp3"),
    "mydonose": ("RADYO MYDONOSE", "http://sc.radyomydonose.com.tr:80/"),
    "slw": ("POWER SLOW", "http://powerapp.live-streams.nl/powerslow.mp3"),
    "banko": ("RADYO BANKO", "http://46.20.3.204/"),
    "bayram": ("GÖNÜL FM", "http://yayin.gonulfm.com:8022/"),
    "kalp": ("KALP FM", "http://yayin.radyokalp.com:8044/"),
    "kafa": ("KAFA FM", "http://kafa.canli-yayin.biz:8000/"),
    "diyanet": ("DİYANET RADYO", "http://yayincdn.diyanet.gov.tr/Radyo1/playlist.m3u8")
}

@app.on_message(filters.command(["radio", "radyo"]) & (filters.group | filters.channel) & ~app.blacklist_filter)
@lang.language()
async def radio_cmd(_, m: types.Message):
    try:
        await m.delete()
    except:
        pass
    await m.reply_text(
        "<b>📻 Radyo oynatmak için bir istasyon seçin:</b>",
        reply_markup=buttons.radio_markup(m.lang)
    )

@app.on_callback_query(filters.regex(r"^radio") & ~app.blacklist_filter)
@lang.language()
async def radio_callback(_, query: types.CallbackQuery):
    data = query.data.split()
    if len(data) < 2:
        return await query.answer()
    
    station_id = data[1]
    if station_id not in STATIONS:
        return await query.answer("Geçersiz istasyon!", show_alert=True)
    
    name, url = STATIONS[station_id]
    await query.answer(f"📻 {name} başlatılıyor...")
    
    chat_id = query.message.chat.id
    user_mention = query.from_user.mention
    
    track = Track(
        id=station_id,
        title=name,
        url=url,
        duration="Canlı",
        duration_sec=0,
        channel_name="Radyo",
        user=user_mention,
        user_id=query.from_user.id,
        file_path=url,
        video=False,
    )
    
    # Mevcut çalanı durdur ve bunu oynat (Radio genellikle hemen başlasın istenir)
    await anon.stop(chat_id)
    
    sent = await query.message.edit_text(f"<b>📻 {name} Oynatılıyor...</b>")
    await anon.play_media(chat_id, sent, track)
