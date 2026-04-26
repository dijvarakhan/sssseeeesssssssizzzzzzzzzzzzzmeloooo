# @The_Team_kumsal tarafından yasal olarak geliştirildi keyifli kullanımlar #kumsalteam
# Copyright (c) 2025 TheHamkerAlone
# Licensed under the MIT License.
# This file is part of KumsalTR


from pyrogram import filters, types

from KumsalTR import anon, app, db, lang
from KumsalTR.helpers import can_manage_vc


from KumsalTR.plugins.quiz import QUIZ_STATE, end_quiz_logic

@app.on_message(filters.command(["son", "durdur", "stop", "bitir"]) & (filters.group | filters.channel) & ~app.blacklist_filter)
@lang.language()
@can_manage_vc
async def _stop(_, m: types.Message):
    chat_id = m.chat.id
    stopped_something = False
    
    # 1. Yarışma Durdurma (Eğer aktifse)
    if chat_id in QUIZ_STATE and QUIZ_STATE[chat_id].get("active"):
        QUIZ_STATE[chat_id]["active"] = False
        QUIZ_STATE[chat_id]["winner_found"].set()
        await end_quiz_logic(chat_id)
        stopped_something = True

    # 2. Müzik Durdurma
    if await db.get_call(chat_id):
        await anon.stop(chat_id)
        stopped_something = True

    if stopped_something:
        await m.reply_text(m.lang["play_stopped"].format(m.from_user.mention))
    else:
        await m.reply_text(m.lang["not_playing"])
