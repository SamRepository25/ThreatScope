from telegram.ext import (
    Application,
    CommandHandler,
)
from telegram.request import HTTPXRequest

from app.config import BOT_TOKEN

from app.handlers.start import start
from app.handlers.help import help_command
from app.handlers.about import about
from app.handlers.version import version
from app.handlers.error import error_handler
from app.handlers.news import news_command
from app.handlers.hackernews import hackernews_command
from app.handlers.bleepingcomputer import bleepingcomputer_command
from app.handlers.securityweek import securityweek_command
from app.handlers.sans import sans_command
from app.handlers.krebs import krebs_command
from app.handlers.darkreading import darkreading_command
from app.handlers.talos import talos_command
from app.handlers.tools import tools_command
from app.handlers.cves import cves_command
from telegram.ext import (
    MessageHandler,
    filters,
)

from app.handlers.fallback import unknown_command


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
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("version", version))
    application.add_handler(CommandHandler("news", news_command))
    application.add_handler(CommandHandler("hackernews", hackernews_command))
    application.add_handler(CommandHandler("bleepingcomputer", bleepingcomputer_command))
    application.add_handler(CommandHandler("securityweek", securityweek_command))
    application.add_handler(CommandHandler("sans", sans_command))
    application.add_handler(CommandHandler("krebs", krebs_command))
    application.add_handler(CommandHandler("darkreading", darkreading_command))
    application.add_handler(CommandHandler("talos", talos_command))
    application.add_handler(CommandHandler("tools", tools_command))
    application.add_handler(CommandHandler("cves", cves_command))
    application.add_error_handler(error_handler)

    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            unknown_command,
        )
    )

    return application