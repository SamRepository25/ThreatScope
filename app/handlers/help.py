from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
🛡 ThreatScope Help

Available Commands

/start - Start ThreatScope
/help - Show this help
/about - About the bot
/version - Current version

More features coming soon...
📰 Security News
🚨 CVEs
🌐 Network Tools
🔍 OSINT
📖 Cheat Sheets
🧠 Daily Learning
"""
    )