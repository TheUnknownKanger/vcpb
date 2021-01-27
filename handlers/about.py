from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from handlers import all_help
from helpers import wrap
from strings import get_string as _

@Client.on_message(
    filters.command("about", "/") & filters.private
)
@wrap
def about(client, message):
    message.reply_text(_("creds")) 

__handlers__ = [
    [
        MessageHandler(
            rules,
            filters.command("about", "/")
            & filters.private
        )
    ]
]
__help__ = {
    "help": [_("help_about"), False]
}
