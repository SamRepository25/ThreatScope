import logging


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    )

    logging.getLogger("httpx").setLevel(logging.WARNING)

    return logging.getLogger("ThreatScope")