from telegram import Update
from telegram.ext import ContextTypes

from app.feeds.sans import get_sans


async def sans_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send the latest SANS ISC news."""

    articles = get_sans()

    if not articles:
        await update.message.reply_text(
            "❌ Unable to fetch SANS ISC news."
        )
        return

    latest = articles[:5]

    message = "🌩️ *SANS Internet Storm Center*\n\n"

    for i, article in enumerate(latest, start=1):
        message += (
            f"{i}. *{article['title']}*\n"
            f"🕒 {article['published']}\n"
            f"🔗 {article['link']}\n\n"
        )

    await update.message.reply_text(
        message,
        parse_mode="Markdown",
        disable_web_page_preview=True,
    )