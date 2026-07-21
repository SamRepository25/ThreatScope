from telegram import Update
from telegram.ext import ContextTypes

from app.feeds.news_engine import get_all_news


async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):

    articles = get_all_news()

    if not articles:
        await update.message.reply_text(
            "❌ Unable to fetch cybersecurity news."
        )
        return

    message = "📰 Latest Cybersecurity News\n\n"

    for article in articles:
        message += (
            f"🌐 {article['source']}\n"
            f"📰 {article['title']}\n"
            f"🔗 {article['link']}\n\n"
        )

    await update.message.reply_text(
        message,
        disable_web_page_preview=True,
    )