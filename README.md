# 🕵️ ThreatScope[ThreatScope](https://t.me/ThreatScopeIntelBot)


> **Cybersecurity Intelligence Assistant for Telegram**

ThreatScope is a Telegram bot that brings cybersecurity news, vulnerability information, and curated security resources into one convenient interface. It helps security enthusiasts, students, and IT professionals stay informed through updates from security publications and the National Vulnerability Database (NVD).

---

## ✨ Features

- 📰 **Aggregated cybersecurity news** — latest articles collected from multiple security publications.
- 🗞️ **Source-specific feeds** — browse news from individual sources.
- 🚨 **CVE updates** — view recent CVEs with severity, CVSS score, publication date, description, and link to the NVD entry.
- 🧰 **Curated security tools** — categorized links for OSINT, network security, web security, malware analysis, password/hash tools, and utilities.
- ⚡ **Async Telegram bot** — responsive command handling with asynchronous handlers.
- 🧵 **News caching** — cache support to reduce repeated feed processing.
- ⏱️ **Rate limiting** — cooldowns for selected commands to help prevent repeated requests.
- 🪵 **Logging** — application logs for troubleshooting.
- 🖥️ **Windows launcher** — start the bot using the included `ThreatScope.bat` file.

---

## 📰 News Sources

ThreatScope includes source-specific news commands for:

| Source | Command |
|---|---|
| The Hacker News | `/hackernews` |
| BleepingComputer | `/bleepingcomputer` |
| SecurityWeek | `/securityweek` |
| SANS Internet Storm Center | `/sans` |
| Krebs on Security | `/krebs` |
| Dark Reading | `/darkreading` |
| Cisco Talos | `/talos` |

The aggregated `/news` command collects recent items from configured feeds.

---

## 🚨 Vulnerability Information

The `/cves` command retrieves recent CVE entries from the **National Vulnerability Database (NVD)** and displays information such as:

- CVE identifier
- Severity and CVSS score, when available
- Published date
- Brief description
- Link to the NVD vulnerability page

ThreatScope is an information aggregator; it does not perform vulnerability scanning or exploit testing.

---

## 🤖 Commands

| Command | Description |
|---|---|
| `/start` | Start the bot |
| `/help` | Show available commands |
| `/about` | Information about ThreatScope |
| `/version` | Show version information |
| `/news` | Aggregated cybersecurity news |
| `/hackernews` | The Hacker News feed |
| `/bleepingcomputer` | BleepingComputer feed |
| `/securityweek` | SecurityWeek feed |
| `/sans` | SANS Internet Storm Center feed |
| `/krebs` | Krebs on Security feed |
| `/darkreading` | Dark Reading feed |
| `/talos` | Cisco Talos feed |
| `/cves` | Recent CVE information |
| `/tools` | Curated cybersecurity tools and resources |

---

## 🧰 Cybersecurity Tools

The `/tools` command provides curated links across categories:

- **OSINT:** Shodan, Censys, VirusTotal, URLScan, WHOIS
- **Network:** Nmap, Wireshark, Angry IP Scanner
- **Web security:** Burp Suite, OWASP ZAP
- **Malware analysis:** ANY.RUN, Hybrid Analysis, Joe Sandbox
- **Password & hashing:** Hashcat, John the Ripper
- **Utilities:** CyberChef, ExifTool, YARA

These are external resources. ThreatScope does not run these tools on behalf of users.

---

## 🧱 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| python-telegram-bot | Telegram bot framework |
| HTTPX / Requests | HTTP requests and API access |
| Feedparser / BeautifulSoup / lxml | Feed and content parsing |
| Flask | Keep-alive web endpoint |
| Rich | Terminal startup display |
| python-dotenv | Environment configuration |
| Git & GitHub | Version control |

---

## 📂 Project Structure

```text
ThreatScope/
├── app/
│   ├── bot.py
│   ├── main.py
│   ├── config.py
│   ├── keep_alive.py
│   ├── cache/
│   ├── feeds/
│   │   ├── cves.py
│   │   ├── news_engine.py
│   │   └── parser.py
│   ├── handlers/
│   │   ├── news.py
│   │   ├── cves.py
│   │   ├── tools.py
│   │   └── ... source-specific handlers
│   └── utils/
│       ├── logger.py
│       └── rate_limiter.py
├── .env.example
├── requirements.txt
├── ThreatScope.bat
└── README.md
```

---

## 🚀 Installation

### Prerequisites

- Python 3.10+ (use a version compatible with the installed dependencies)
- Git
- A Telegram bot token from [BotFather](https://t.me/BotFather)

### 1. Clone the repository

```bash
git clone https://github.com/SamRepository25/ThreatScope.git
cd ThreatScope
```

### 2. Create and activate a virtual environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the bot

Copy `.env.example` to `.env` and add your Telegram bot token. Keep your `.env` file private.

Example:

```env
BOT_TOKEN=replace_with_your_bot_token
```

---

## ▶️ Run ThreatScope

**Windows:** Launch `ThreatScope.bat` from the project folder.

Or run the application from the activated environment:

```bash
python -m app.main
```

ThreatScope currently runs as a local process. It is available while the host system is powered on and the bot process is running. It is **not guaranteed to be hosted 24/7**.

---

## 🔒 Security & Privacy

- Keep bot tokens, API keys, and other credentials out of Git.
- Use the provided `.env.example` as a configuration template, not for real secrets.
- ThreatScope aggregates publicly available information and links to external sources.
- The bot uses in-memory user information for command rate limiting; this is not intended as persistent user profiling.
- Use linked tools and security resources only on systems you own or are explicitly authorized to assess.

See [SECURITY.md](SECURITY.md) for vulnerability reporting guidance.

### Legal Documents

- [Privacy Policy](PRIVACY.md)
- [Terms of Use](TERMS.md)
- [Disclaimer](DISCLAIMER.md)

---

## ⚠️ Limitations

- News and CVE data depend on third-party feeds and APIs being available.
- Feed formats, network conditions, and source changes can affect results.
- CVE entries are informational; always consult the original advisory and vendor guidance before making security decisions.
- ThreatScope is not a vulnerability scanner, SIEM, or automated incident-response platform.
- Local hosting means bot availability depends on the host and running process.

---

## 🧪 Tests

The repository includes tests for feed parsing, news aggregation, and CVE processing. Run the test suite from the repository root:

```bash
python -m pytest
```

---

## 📜 License

ThreatScope is licensed under the **Apache License 2.0**. See [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

**B SIMAK AHMED**  
GitHub: [@SamRepository25](https://github.com/SamRepository25)

---

## 🤝 Contributions

Suggestions, bug reports, and contributions are welcome. Please include clear reproduction steps and relevant logs when reporting an issue—and **never include secrets or bot tokens**.

---

<div align="center">

**ThreatScope — Cybersecurity intelligence at your fingertips.** 🛡️

</div>
