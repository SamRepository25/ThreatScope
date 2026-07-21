from telegram import BotCommand
from telegram.ext import (
    Application,
    CommandHandler,
)

from app.config import BOT_TOKEN

from app.handlers.start import start
from app.handlers.help import help_command
from app.handlers.about import about
from app.handlers.version import version
from app.handlers.error import error_handler
from app.handlers.news import news


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

    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("version", version))
    application.add_handler(CommandHandler("news", news))

    application.add_error_handler(error_handler)

    return application