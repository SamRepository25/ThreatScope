from telegram import Update
from telegram.ext import ContextTypes

from app.feeds.krebs import get_krebs


async def krebs_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send the latest Krebs on Security articles."""

    articles = get_krebs()

    if not articles:
        await update.message.reply_text(
            "❌ Unable to fetch Krebs on Security articles."
        )
        return

    latest = articles[:5]

    message = "🕵️ *Krebs on Security*\n\n"

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