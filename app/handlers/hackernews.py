from telegram import Update
from telegram.ext import ContextTypes

from app.feeds.hackernews import get_hackernews


async def hackernews_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send the latest Hacker News articles."""

    articles = get_hackernews()

    if not articles:
        await update.message.reply_text("❌ Unable to fetch The Hacker News.")
        return

    latest = articles[:5]

    message = "📰 *The Hacker News*\n\n"

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