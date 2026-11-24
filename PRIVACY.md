# ThreatScope Privacy Policy

**Effective date:** November 24, 2026

ThreatScope is an independent Telegram cybersecurity-intelligence bot that provides security news, vulnerability information, threat-awareness content, and links to external resources.

## Information We Process

When you interact with ThreatScope, the Telegram platform and the bot may make available information such as your Telegram chat ID, username (if set), message content, and basic interaction details. ThreatScope uses chat IDs to deliver requested responses and, if you subscribe, scheduled intelligence broadcasts.

The bot's intelligence feature stores subscriber chat IDs and subscription timestamps in a local SQLite database. It also stores identifiers for previously processed CVEs and CISA Known Exploited Vulnerabilities (KEV) entries to avoid duplicate alerts, and a record of alert events (including timestamps, alert types, titles, and details). The application may keep operational logs for troubleshooting. Selected command rate-limit information is held in memory.

## Subscriptions and Deletion

Use `/unsubscribe` to remove your chat ID from the bot's broadcast subscriber list. You may continue using other bot commands after unsubscribing. Unsubscribing does not automatically erase other application records, such as alert history, operational logs, or Telegram's own records. For questions or deletion requests regarding data controlled by this project, contact the project maintainer through the repository: https://github.com/SamRepository25/ThreatScope

## Third-Party Services and Sources

ThreatScope operates through Telegram and retrieves content from external cybersecurity feeds, APIs, and websites, including news publishers, the National Vulnerability Database (NVD), and CISA's Known Exploited Vulnerabilities catalog. These third parties have their own privacy policies, terms, availability, and data practices. If the bot is hosted by a third-party provider, that provider may process operational data according to its own terms and policies.

## Data Security and Retention

ThreatScope is a personal project. Reasonable measures are used to avoid exposing credentials and to limit data handling, but no service or transmission can be guaranteed completely secure. Database records and logs may remain until they are manually cleaned up or removed as part of maintenance. Do not send passwords, secrets, private files, or sensitive personal information to the bot.

## Children's Privacy

ThreatScope is not designed to knowingly collect personal information from children. If you believe a child has provided information to the project, contact the maintainer through the repository.

## Policy Changes and Contact

This policy may be updated as ThreatScope's features or data practices change. The current version will be published in this repository. For privacy questions or requests, open a repository issue at https://github.com/SamRepository25/ThreatScope/issues.

---
ThreatScope is an independent project and is not affiliated with Telegram, NVD, CISA, or the news sources it links to.
