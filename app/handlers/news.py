import asyncio

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import ContextTypes

from app.feeds.news_engine import get_all_news
from app.utils.rate_limiter import is_rate_limited


NEWS_COOLDOWN = 15


async def news_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send the latest cybersecurity news."""

    user_id = update.effective_user.id

    limited, remaining = is_rate_limited(
        user_id,
        "news",
        NEWS_COOLDOWN,
    )

    if limited:
        await update.message.reply_text(
            f"⏳ Please wait {remaining} seconds before using /news again."
        )
        return

    loading_message = await update.message.reply_text(
        "🛡️ <b>ThreatScope</b>\n\n"
        "🔄 Fetching the latest cybersecurity news from multiple trusted sources...\n\n"
        "⏳ Please wait...",
        parse_mode="HTML",
    )

    articles = await asyncio.to_thread(get_all_news, limit=10)

    if not articles:
        await loading_message.edit_text(
            "❌ Unable to fetch the latest cybersecurity news."
        )
        return

    message = "🛡️ *Latest Cybersecurity News*\n\n"

    buttons = []

    for i, article in enumerate(articles, start=1):
        message += (
            f"*{i}. {article['title']}*\n"
            f"🏢 {article['source']}\n"
            f"🕒 {article['published']}\n\n"
        )

        buttons.append(
            [
                InlineKeyboardButton(
                    text="📖 Read Article",
                    url=article["link"],
                )
            ]
        )

    reply_markup = InlineKeyboardMarkup(buttons)

    await loading_message.edit_text(
        text=message,
        parse_mode="Markdown",
        reply_markup=reply_markup,
        disable_web_page_preview=True,
    )