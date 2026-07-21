from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """
🛡 ThreatScope Help

/start - Start the bot
/help - Show help
/about - About the bot
/version - Current version

Upcoming

📰 Security News
🚨 CVEs
🌐 Network Tools
🔍 OSINT
📖 Cheat Sheets
🧠 Daily Learning
"""
    )