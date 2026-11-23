from telegram import Update
from telegram.ext import ContextTypes

from app.feeds.darkreading import get_darkreading


async def darkreading_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send the latest Dark Reading articles."""

    articles = get_darkreading()

    if not articles:
        await update.message.reply_text(
            "❌ Unable to fetch Dark Reading articles."
        )
        return

    latest = articles[:5]

    message = "🌑 *Dark Reading*\n\n"

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