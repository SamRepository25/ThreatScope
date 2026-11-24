from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    welcome_message = (
        "🛡️ <b>Welcome to ThreatScope</b>\n\n"
        "Your independent cybersecurity intelligence assistant \u2014 aggregating "
        "news, CVEs, and curated tools in one place.\n\n"
        "<b>What you can do:</b>\n\n"
        "📰 /news \u2014 Latest cybersecurity news\n"
        "📋 /briefing — Daily security briefing\n"
        "🎯 /threat — Threat of the day\n"
        "🔔 /subscribe — Subscribe to alerts\n"
        "🔕 /unsubscribe — Stop alerts\n"
        "🚨 /cves \u2014 Latest CVEs\n"
        "🛠️ /tools \u2014 Cybersecurity, networking & OSINT tools\n"
        "\u2139\ufe0f /about \u2014 About ThreatScope, disclaimers & privacy\n"
        "\u2753 /help \u2014 Full command list\n\n"
        "For informational and educational use. See /about for details.\n\n"
        "<b>Version:</b> v1.0.0"
    )

    await update.message.reply_text(
        welcome_message,
        parse_mode="HTML",
    )
