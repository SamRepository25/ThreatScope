from telegram import Update
from telegram.ext import ContextTypes


async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle unknown text messages."""

    if update.message is None:
        return

    await update.message.reply_text(
        "🛡️ I'm ThreatScope, your Cybersecurity Intelligence Assistant.\n\n"
        "I currently respond to commands only.\n\n"
        "📌 Type /help to see all available commands."
    )