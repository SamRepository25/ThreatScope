from telegram import Update
from telegram.ext import ContextTypes

from app.feeds.securityweek import get_securityweek


async def securityweek_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    articles = get_securityweek()

    if not articles:
        await update.message.reply_text(
            "❌ Unable to fetch SecurityWeek."
        )
        return

    message = "🛡️ *SecurityWeek*\n\n"

    for i, article in enumerate(articles[:5], start=1):
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