from telegram import Update
from telegram.ext import ContextTypes


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = (
        "🛡️ <b>ThreatScope</b>\n\n"

        "<b>Version:</b> v1.0.0\n\n"

        "Personal Cybersecurity Intelligence Assistant\n\n"

        "<b>Features</b>\n\n"

        "📰 Latest Cybersecurity News\n"
        "🚨 Latest CVEs\n"
        "🔎 OSINT Resources\n"
        "🌐 Networking Tools\n"
        "🛠️ Cybersecurity Tools\n\n"

        "ℹ️ ThreatScope aggregates publicly available cybersecurity news, CVE data, "
        "and tools for informational and educational purposes. It is an independent "
        "project and is not affiliated with, endorsed by, or sponsored by any of the "
        "news sources, CVE data sources, or tools it references.\n\n"

        "🔒 ThreatScope does not persistently store user messages or personal data. "
        "Minimal user information is held temporarily in memory only for command "
        "rate limiting and is cleared when the bot restarts.\n\n"

        "Built with Python."
    )

    await update.message.reply_text(
        message,
        parse_mode="HTML",
    )