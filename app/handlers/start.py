from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """
🛡 Welcome to ThreatScope

Your Personal Cybersecurity Intelligence Assistant.

Available Commands

/start
/help
/about
/version

More features are coming soon...
"""
    )