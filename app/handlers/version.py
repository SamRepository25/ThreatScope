from telegram import Update
from telegram.ext import ContextTypes


async def version(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = (
        "🛡️ <b>ThreatScope</b>\n\n"

        "<b>Version:</b> v1.0.0\n\n"

        "Status: ✅ Stable Release"
    )

    await update.message.reply_text(
        message,
        parse_mode="HTML",
    )