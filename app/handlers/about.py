from telegram import Update
from telegram.ext import ContextTypes


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
🛡 ThreatScope

Version: v0.1.0

Personal Cybersecurity Intelligence Assistant

Features
• Security News
• Latest CVEs
• Network Tools
• OSINT
• Cheat Sheets
• Daily Learning

Built with Python.
"""
    )