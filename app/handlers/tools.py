from telegram import Update
from telegram.ext import ContextTypes


async def tools_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Display useful cybersecurity tools."""

    message = (
        "🛠️ <b>Cybersecurity Tools</b>\n\n"

        "🌐 <b>OSINT</b>\n"
        "• <a href='https://www.shodan.io'>Shodan</a>\n"
        "• <a href='https://search.censys.io'>Censys</a>\n"
        "• <a href='https://www.virustotal.com'>VirusTotal</a>\n"
        "• <a href='https://urlscan.io'>URLScan</a>\n"
        "• <a href='https://who.is'>WHOIS</a>\n\n"

        "🌍 <b>Network</b>\n"
        "• <a href='https://nmap.org'>Nmap</a>\n"
        "• <a href='https://www.wireshark.org'>Wireshark</a>\n"
        "• <a href='https://angryip.org'>Angry IP Scanner</a>\n\n"

        "🌐 <b>Web Security</b>\n"
        "• <a href='https://portswigger.net/burp'>Burp Suite</a>\n"
        "• <a href='https://www.zaproxy.org'>OWASP ZAP</a>\n\n"

        "🦠 <b>Malware Analysis</b>\n"
        "• <a href='https://any.run'>ANY.RUN</a>\n"
        "• <a href='https://www.hybrid-analysis.com'>Hybrid Analysis</a>\n"
        "• <a href='https://www.joesecurity.org'>Joe Sandbox</a>\n\n"

        "🔐 <b>Password & Hashing</b>\n"
        "• <a href='https://hashcat.net/hashcat'>Hashcat</a>\n"
        "• <a href='https://www.openwall.com/john'>John the Ripper</a>\n\n"

        "⚙️ <b>Utilities</b>\n"
        "• <a href='https://gchq.github.io/CyberChef'>CyberChef</a>\n"
        "• <a href='https://exiftool.org'>ExifTool</a>\n"
        "• <a href='https://virustotal.github.io/yara'>YARA</a>"
    )

    await update.message.reply_text(
        message,
        parse_mode="HTML",
        disable_web_page_preview=True,
    )