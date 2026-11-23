import asyncio

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import ContextTypes

from app.feeds.cves import get_cves
from app.utils.rate_limiter import is_rate_limited


CVE_COOLDOWN = 10


async def cves_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    limited, remaining = is_rate_limited(
        user_id,
        "cves",
        CVE_COOLDOWN,
    )

    if limited:
        await update.message.reply_text(
            f"⏳ Please wait {remaining} seconds before using /cves again."
        )
        return

    loading = await update.message.reply_text(
        "🚨 <b>ThreatScope</b>\n\n"
        "🔄 Fetching latest CVEs...\n\n"
        "⏳ Please wait...",
        parse_mode="HTML",
    )

    cves = await asyncio.to_thread(get_cves)

    if not cves:
        await loading.edit_text("❌ Unable to fetch CVEs.")
        return

    message = "🚨 <b>Latest CVEs</b>\n\n"

    buttons = []

    for cve in cves:

        severity_icon = {
            "CRITICAL": "🔴",
            "HIGH": "🟠",
            "MEDIUM": "🟡",
            "LOW": "🟢",
        }.get(cve["severity"], "⚪")

        description = cve["description"][:180]

        if len(cve["description"]) > 180:
            description += "..."

        message += (
            f"<b>{cve['id']}</b>\n"
            f"{severity_icon} {cve['severity']} ({cve['score']})\n"
            f"📅 {cve['published']}\n"
            f"{description}\n\n"
        )

        buttons.append(
            [
                InlineKeyboardButton(
                    text=f"📖 {cve['id']}",
                    url=cve["link"],
                )
            ]
        )

    await loading.edit_text(
        message,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True,
    )