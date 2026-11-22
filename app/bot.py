from telegram import BotCommand
from telegram.ext import (
    Application,
    CommandHandler,
)
from telegram.request import HTTPXRequest

from app.config import BOT_TOKEN
from app.handlers.about import about
from app.handlers.error import error_handler
from app.handlers.help import help_command
from app.handlers.news import news  # change to news_command if news.py defines news_command
from app.handlers.start import start
from app.handlers.version import version


async def post_init(application: Application):
    commands = [
        BotCommand("start", "Start ThreatScope"),
        BotCommand("help", "Show help"),
        BotCommand("about", "About ThreatScope"),
        BotCommand("version", "Bot version"),
        BotCommand("news", "Latest cybersecurity news"),
    ]
    await application.bot.set_my_commands(commands)


def create_application():
    request = HTTPXRequest(
        connect_timeout=30.0,
        read_timeout=30.0,
        write_timeout=30.0,
        pool_timeout=30.0,
    )

    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .request(request)
        .post_init(post_init)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("version", version))
    application.add_handler(CommandHandler("news", news))  # change to news_command if needed

    application.add_error_handler(error_handler)

    return application
