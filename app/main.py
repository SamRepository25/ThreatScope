from app.bot import create_application
from app.utils.logger import setup_logger


def main():
    logger = setup_logger()

    logger.info("Starting ThreatScope...")

    application = create_application()

    logger.info("ThreatScope is running...")

    application.run_polling()


if __name__ == "__main__":
    main()