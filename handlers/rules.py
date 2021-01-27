from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from handlers import all_help
from helpers import wrap
from strings import get_string as _

@Client.on_message(
    filters.command("rules", "/") & filters.private
)
@wrap
def rules(client, message):
    message.reply_text(_("rules")) 

__handlers__ = [
    [
        MessageHandler(
            rules,
            filters.command("rules", "/")
            & filters.private
        )
    ]
]
__help__ = {
    "help": [_("help_rules"), False]
}
