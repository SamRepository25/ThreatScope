# Security Policy

## Overview

ThreatScope is a personal cybersecurity intelligence Telegram bot that aggregates security news, CVEs, OSINT resources, networking tools, and learning resources.

Security is an important part of the project. This policy explains how to report security vulnerabilities responsibly.

## Supported Versions

Security fixes are currently focused on the latest version of ThreatScope available in the `main` branch and the latest published release.

| Version | Supported |
| --- | --- |
| Latest release | ✅ |
| `main` | ✅ |
| Older releases | ❌ |

## Reporting a Vulnerability

If you discover a security vulnerability in ThreatScope, please **do not open a public GitHub issue** with sensitive vulnerability details.

Please report the issue privately through GitHub's security reporting features available for this repository. Include:

- A clear description of the vulnerability
- The affected component, file, command, or feature
- Steps to reproduce the issue
- The potential security impact
- Any proof-of-concept needed to reproduce the issue safely
- Suggested remediation, if known

Please allow reasonable time for the issue to be reviewed and addressed before publicly disclosing vulnerability details.

## Sensitive Information

Never include secrets in public issues, pull requests, commits, or discussions. This includes:

- Telegram bot tokens
- API keys
- Passwords
- Access tokens
- Database credentials
- Private configuration values

Use environment variables for secrets and keep local `.env` files out of version control.

## Security Research

ThreatScope is intended for legitimate cybersecurity education, research, and defensive security purposes. Security testing should only be performed against systems and services you are authorized to test.

## Acknowledgements

Responsible security researchers who report valid vulnerabilities may be acknowledged in the project's release notes or security documentation, subject to their preference.

Thank you for helping keep ThreatScope secure.
