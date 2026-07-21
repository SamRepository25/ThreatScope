from telegram import Update
from telegram.ext import ContextTypes


async def version(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡 ThreatScope\n\nVersion: v0.1.0"
    )