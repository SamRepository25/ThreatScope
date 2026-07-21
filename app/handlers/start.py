from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡 Welcome to ThreatScope!\n\n"
        "Your Personal Cybersecurity Intelligence Assistant.\n\n"
        "Version: v0.1.0"
    )