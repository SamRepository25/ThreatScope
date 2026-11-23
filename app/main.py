from app.bot import create_application
from app.utils.logger import setup_logger

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from app.keep_alive import keep_alive

import platform
import sys
import httpx

console = Console()

VERSION = "1.0.0"


def show_banner(status="🟡 STARTING"):
    content = Text()

    content.append(f"🛡️ ThreatScope v{VERSION}\n", style="bold cyan")
    content.append("Cybersecurity Intelligence Assistant\n\n", style="bold white")

    content.append("Status", style="bold green")
    content.append("        : ")
    content.append(f"{status}\n", style="bold")

    content.append("Python", style="bold green")
    content.append("        : ")
    content.append(f"{sys.version.split()[0]}\n")

    content.append("Platform", style="bold green")
    content.append("      : ")
    content.append(f"{platform.system()}\n")

    content.append("Mode", style="bold green")
    content.append("          : ")
    content.append("Polling\n")

    content.append("News Sources", style="bold green")
    content.append("  : ")
    content.append("7\n")

    content.append("CVE Feed", style="bold green")
    content.append("      : ")
    content.append("Enabled")

    panel = Panel(
        Align.center(content),
        title="[bold green]STARTUP[/bold green]",
        border_style="cyan",
        width=60,
        expand=False,
    )

    console.clear()
    console.print()
    console.print(Align.center(panel))
    console.print()


def main():
    logger = setup_logger()

    # Show startup state
    show_banner("🟡 STARTING")

    logger.info("Starting ThreatScope...")

    try:
        # Quick internet connectivity check
        httpx.get("https://api.telegram.org", timeout=5)

        # Connected successfully
        show_banner("🟢 ONLINE")

        application = create_application()
        keep_alive()

        logger.info("ThreatScope is running...")

        application.run_polling()

    except Exception:
        # No internet / Telegram unreachable
        show_banner("🔴 OFFLINE")

        logger.error(
            "Unable to connect to Telegram. "
            "Please check your internet connection."
        )


if __name__ == "__main__":
    main()