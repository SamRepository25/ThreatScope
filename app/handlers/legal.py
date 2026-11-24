from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


LEGAL_PAGES = {
    "privacy": (
        "🔒 <b>ThreatScope Privacy Policy</b>\n\n"
        "Review how ThreatScope handles information and data.\n",
        "https://github.com/SamRepository25/ThreatScope/blob/main/PRIVACY.md",
        "View Privacy Policy",
    ),
    "terms": (
        "📜 <b>ThreatScope Terms of Use</b>\n\n"
        "Review the terms for using ThreatScope.\n",
        "https://github.com/SamRepository25/ThreatScope/blob/main/TERMS.md",
        "View Terms of Use",
    ),
    "disclaimer": (
        "⚠️ <b>ThreatScope Disclaimer</b>\n\n"
        "ThreatScope provides cybersecurity information for informational and educational purposes only.\n",
        "https://github.com/SamRepository25/ThreatScope/blob/main/DISCLAIMER.md",
        "View Disclaimer",
    ),
}


async def legal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command = update.message.text.split()[0].lstrip("/").split("@")[0].lower()
    message, url, button_text = LEGAL_PAGES.get(command, LEGAL_PAGES["privacy"])
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(button_text, url=url)]
    ])
    await update.message.reply_text(message, parse_mode="HTML", reply_markup=keyboard)
