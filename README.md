# 🕵️ [ThreatScope](https://t.me/ThreatScopeIntelBot)

> **Cybersecurity Intelligence Assistant for Telegram**

ThreatScope is an independent Telegram bot that brings cybersecurity news, vulnerability information, curated security resources, and security alerts into one convenient interface. It helps students, security enthusiasts, and IT professionals stay informed.

---

## ✨ Features

- 📰 Aggregated cybersecurity news from multiple publications
- 🗞️ Source-specific news feeds
- 🚨 Recent CVE information from the National Vulnerability Database (NVD)
- 📋 Daily security briefing combining top news and CVEs
- 🎯 Threat of the Day with practical awareness tips
- 🔔 Subscription-based cybersecurity intelligence alerts
- ⚠️ Critical CVE and CISA Known Exploited Vulnerabilities (KEV) monitoring
- 🧰 Curated OSINT, network, web security, malware analysis, and utility resources
- ⚡ Asynchronous Telegram command handling
- 🧵 News caching and command rate limiting
- 🪵 Logging for troubleshooting
- 🖥️ Windows launcher included

---

## 🤖 Commands

### Main commands (Telegram command menu)

| Command | Description |
|---|---|
| `/start` | Start ThreatScope |
| `/help` | View all commands |
| `/news` | Latest cybersecurity news |
| `/briefing` | Daily security briefing (news and recent CVEs) |
| `/threat` | Threat of the day |
| `/subscribe` | Subscribe to intelligence alerts |
| `/unsubscribe` | Unsubscribe from alerts |
| `/privacy` | Privacy policy |
| `/terms` | Terms of use |
| `/disclaimer` | Legal disclaimer |

### Additional commands

| Command | Description |
|---|---|
| `/about` | About ThreatScope |
| `/version` | Version information |
| `/alerts` | View recent broadcast alerts |
| `/cves` | Recent CVE information |
| `/tools` | Curated cybersecurity tools and resources |
| `/hackernews` | The Hacker News feed |
| `/bleepingcomputer` | BleepingComputer feed |
| `/securityweek` | SecurityWeek feed |
| `/sans` | SANS Internet Storm Center feed |
| `/krebs` | Krebs on Security feed |
| `/darkreading` | Dark Reading feed |
| `/talos` | Cisco Talos feed |

---

## 📰 News Sources

ThreatScope provides aggregated news and individual source feeds:

| Source | Command |
|---|---|
| The Hacker News | `/hackernews` |
| BleepingComputer | `/bleepingcomputer` |
| SecurityWeek | `/securityweek` |
| SANS Internet Storm Center | `/sans` |
| Krebs on Security | `/krebs` |
| Dark Reading | `/darkreading` |
| Cisco Talos | `/talos` |

The `/news` command combines recent items from configured feeds.

---

## 🛡️ Intelligence & Alerts

- **Daily briefing:** `/briefing` combines top cybersecurity news and recent CVEs.
- **Threat of the day:** `/threat` provides a rotating security threat and awareness guidance.
- **Subscriptions:** Use `/subscribe` and `/unsubscribe` to manage broadcast alerts.
- **Critical CVE monitoring:** Checks for CVEs with CVSS scores of 9.0 or higher.
- **CISA KEV monitoring:** Tracks additions to the Known Exploited Vulnerabilities catalog.
- **Recent alerts:** `/alerts` displays the latest recorded broadcast alerts.

Scheduled subscriber briefings and threat updates are sent daily at approximately 9:00 AM and 9:10 AM India Standard Time. Critical CVE monitoring runs hourly and CISA KEV monitoring runs every 30 minutes.

---

## 🚨 Vulnerability Information

The `/cves` command retrieves recent CVE entries from the National Vulnerability Database (NVD), including available details such as:

- CVE identifier
- Severity and CVSS score
- Published date
- Brief description
- Link to the NVD entry

ThreatScope is an information aggregator; it does not perform vulnerability scanning or exploit testing.

---

## 🧰 Cybersecurity Tools

The `/tools` command provides curated external resources across categories:

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
| APScheduler | Scheduled intelligence tasks |
| SQLite | Local alert/subscriber data |
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
│   ├── intelligence.py
│   ├── cache/
│   ├── feeds/
│   │   ├── cves.py
│   │   ├── news_engine.py
│   │   └── parser.py
│   ├── handlers/
│   │   ├── news.py
│   │   ├── cves.py
│   │   ├── tools.py
│   │   ├── legal.py
│   │   └── ... source-specific handlers
│   └── utils/
│       ├── logger.py
│       └── rate_limiter.py
├── data/
├── .env.example
├── requirements.txt
├── ThreatScope.bat
└── README.md
```

---

## 🚀 Installation

### Prerequisites

- Python 3.10+
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

## 🔒 Security, Privacy & Legal

- Keep bot tokens, API keys, and other credentials out of Git.
- Use `.env.example` as a configuration template, not for real secrets.
- ThreatScope aggregates publicly available information and links to external sources.
- Subscriber chat IDs are stored locally in the SQLite database for alert delivery.
- Use linked tools and security resources only on systems you own or are explicitly authorized to assess.

Legal documents:

- [Privacy Policy](PRIVACY.md)
- [Terms of Use](TERMS.md)
- [Disclaimer](DISCLAIMER.md)

See [SECURITY.md](SECURITY.md) for vulnerability reporting guidance.

---

## ⚠️ Limitations

- News and CVE data depend on third-party feeds and APIs being available.
- Feed formats, network conditions, and source changes can affect results.
- CVE entries are informational; consult original advisories and vendor guidance before making security decisions.
- ThreatScope is not a vulnerability scanner, SIEM, or automated incident-response platform.
- Local hosting means bot availability depends on the host and running process.

---

## 🧪 Tests

Run the test suite from the repository root:

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

Suggestions, bug reports, and contributions are welcome. Include clear reproduction steps and relevant logs when reporting issues—and **never include secrets or bot tokens**.

---

<div align="center">

**ThreatScope — Cybersecurity intelligence at your fingertips.** 🕵️

</div>
