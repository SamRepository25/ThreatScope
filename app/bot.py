from telegram.ext import Application, CommandHandler

from app.config import BOT_TOKEN
from app.handlers.start import start
from app.handlers.help import help_command


def create_application() -> Application:
    """
    Create and configure the Telegram application.
    """

    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    return application