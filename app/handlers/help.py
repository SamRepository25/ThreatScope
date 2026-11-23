from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = (
        "🛡️ <b>ThreatScope Help</b>\n\n"

        "<b>General</b>\n"
        "/start - Start ThreatScope\n"
        "/help - Show available commands\n"
        "/about - About ThreatScope\n"
        "/version - Version information\n\n"

        "<b>Cybersecurity News</b>\n"
        "/news - Latest cybersecurity news\n"
        "/hackernews - The Hacker News\n"
        "/bleepingcomputer - BleepingComputer\n"
        "/securityweek - SecurityWeek\n"
        "/sans - SANS ISC\n"
        "/krebs - Krebs on Security\n"
        "/darkreading - Dark Reading\n"
        "/talos - Cisco Talos\n\n"

        "<b>Resources</b>\n"
        "/tools - Cybersecurity tools\n"
        "/cves - Latest CVEs"
    )

    await update.message.reply_text(
        message,
        parse_mode="HTML",
    )