from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helpers import wrap
from strings import get_string as _


@Client.on_message(
    filters.command("start", "/") & filters.private
)
@wrap
def start(client, message):
    message.reply_text(
        _("start_1"),
        reply_markup=InlineKeyboardMarkup(
          ##  [[InlineKeyboardButton(
          ##      _("Rules"), callback_data="rulesall")]], 
           [[InlineKeyboardButton(
                _("Streaming Chat ♥"), url="https://t.me/MysteriousGangSupport")]],
            [[InlineKeyboardButton(
                _("start_2"), switch_inline_query_current_chat="")]],
        ) 
    )

# @Client.on_callback_query()
# def rulesall(client, callback_query):
#    callback_query.answer(text=rules)

__help__ = {
    "start": [_("help_start"), False]
}
