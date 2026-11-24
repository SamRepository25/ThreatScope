import asyncio
import html
import json
import logging
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import httpx
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram import Update
from telegram.ext import Application, ContextTypes

from app.feeds.cves import get_cves
from app.feeds.news_engine import get_all_news

LOG = logging.getLogger(__name__)
IST = ZoneInfo("Asia/Kolkata")
DB_PATH = Path("data/threatscope_intelligence.db")
KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
_scheduler = None

THREATS = [
    ("Phishing", "Fraudulent messages or websites try to trick people into revealing credentials, payment details, or sensitive information. Verify sender identity and avoid unexpected links."),
    ("Ransomware", "Malware encrypts files or disrupts systems and demands payment. Keep offline backups, patch systems, and use multi-factor authentication."),
    ("Credential stuffing", "Attackers reuse leaked passwords across services. Unique passwords and MFA help prevent account takeover."),
    ("Zero-day vulnerability", "A flaw may be exploited before a patch is available. Reduce exposure, monitor vendor advisories, and apply mitigations promptly."),
    ("Business email compromise", "Attackers impersonate trusted people to redirect payments or request sensitive data. Confirm unusual requests through a separate channel."),
    ("DDoS", "A distributed denial-of-service attack overwhelms a service with traffic. Resilience, filtering, and upstream response plans can reduce impact."),
    ("Malicious QR codes", "QR codes can lead to phishing pages or unsafe downloads. Check the destination before opening and avoid QR codes from unknown sources."),
    ("Supply-chain compromise", "An attacker targets software, vendors, or update channels to reach downstream users. Verify updates and inventory trusted dependencies."),
    ("Insider threat", "Risk can arise from misuse of legitimate access, accidental or intentional. Least privilege and audit logging help detect unusual activity."),
    ("Social engineering", "Attackers manipulate people into sharing information or taking unsafe actions. Pause, verify requests, and report suspicious contact."),
]


def _db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS subscribers (chat_id INTEGER PRIMARY KEY, joined_at TEXT NOT NULL)")
    conn.execute("CREATE TABLE IF NOT EXISTS seen_items (kind TEXT NOT NULL, item_id TEXT NOT NULL, PRIMARY KEY(kind,item_id))")
    conn.execute("CREATE TABLE IF NOT EXISTS alert_log (id INTEGER PRIMARY KEY AUTOINCREMENT, created_at TEXT NOT NULL, kind TEXT NOT NULL, title TEXT NOT NULL, details TEXT NOT NULL)")
    return conn



def _subscriber_ids():
    with _db() as conn:
        return [row[0] for row in conn.execute("SELECT chat_id FROM subscribers")]



def _subscribe(chat_id):
    with _db() as conn:
        conn.execute("INSERT OR IGNORE INTO subscribers(chat_id,joined_at) VALUES(?,?)", (chat_id, datetime.now(IST).isoformat()))


def _unsubscribe(chat_id):
    with _db() as conn:
        conn.execute("DELETE FROM subscribers WHERE chat_id=?", (chat_id,))


def _is_seen(kind, item_id):
    with _db() as conn:
        return conn.execute("SELECT 1 FROM seen_items WHERE kind=? AND item_id=?", (kind, str(item_id))).fetchone() is not None


def _mark_seen(kind, item_id):
    with _db() as conn:
        conn.execute("INSERT OR IGNORE INTO seen_items(kind,item_id) VALUES(?,?)", (kind, str(item_id)))


def _log_alert(kind, title, details):
    with _db() as conn:
        conn.execute("INSERT INTO alert_log(created_at,kind,title,details) VALUES(?,?,?,?)", (datetime.now(IST).isoformat(), kind, title, details))



async def _broadcast(app, kind, title, message):
    _log_alert(kind, title, message)
    for chat_id in _subscriber_ids():
        try:
            await app.bot.send_message(chat_id=chat_id, text=message, parse_mode="HTML", disable_web_page_preview=True)
        except Exception as exc:
            LOG.warning("Alert delivery failed for %s: %s", chat_id, exc)


async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    _subscribe(chat_id)
    await update.effective_message.reply_text("✅ You are subscribed to ThreatScope intelligence alerts. Use /unsubscribe anytime.")


async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _unsubscribe(update.effective_chat.id)
    await update.effective_message.reply_text("You have been unsubscribed from broadcast alerts. You can still use all commands.")


async def alerts_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with _db() as conn:
        rows = conn.execute("SELECT created_at,kind,title FROM alert_log ORDER BY id DESC LIMIT 5").fetchall()
    if not rows:
        await update.effective_message.reply_text("No recent ThreatScope broadcast alerts.")
        return
    text = "<b>Recent ThreatScope Alerts</b>\n\n" + "\n".join(f"• <b>{html.escape(kind)}</b> — {html.escape(title)}\n  {html.escape(ts[:16])}" for ts, kind, title in rows)
    await update.effective_message.reply_text(text, parse_mode="HTML")


async def threat_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day = datetime.now(IST).timetuple().tm_yday
    name, description = THREATS[(day - 1) % len(THREATS)]
    await update.effective_message.reply_text(f"🛡️ <b>Threat of the Day</b>\n\n<b>{html.escape(name)}</b>\n{html.escape(description)}\n\n<em>Awareness tip: verify, patch, and report suspicious activity.</em>", parse_mode="HTML")


async def briefing_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text("⏳ Preparing the latest security briefing…")
    try:
        articles = await asyncio.to_thread(get_all_news, 5)
        cves = await asyncio.to_thread(get_cves)
        today = datetime.now(IST).strftime("%d %b %Y")
        lines = [f"🛡️ <b>ThreatScope Daily Briefing — {today}</b>", "", "<b>Top cybersecurity news</b>"]
        for article in (articles or [])[:5]:
            title = html.escape(str(article.get("title", "Untitled")))
            link = html.escape(str(article.get("link", "")), quote=True)
            source = html.escape(str(article.get("source", "Source")))
            lines.append(f"• <a href='{link}'>{title}</a> <i>({source})</i>")
        lines.extend(["", "<b>Recent CVEs</b>"])
        for cve in (cves or [])[:3]:
            title = html.escape(str(cve.get("id", "CVE")))
            severity = html.escape(str(cve.get("severity", "Unknown")))
            score = html.escape(str(cve.get("score", "N/A")))
            link = html.escape(str(cve.get("link", "")), quote=True)
            lines.append(f"• <a href='{link}'>{title}</a> — {severity} ({score})")
        lines.append("\n<i>Informational only. Review source advisories for details.</i>")
        message = "\n".join(lines)
        await update.effective_message.reply_text(message[:4000], parse_mode="HTML", disable_web_page_preview=True)
    except Exception as exc:
        LOG.exception("Daily briefing generation failed")
        await update.effective_message.reply_text("Unable to prepare the briefing right now. Please try again later.")


async def _critical_cve_job(app: Application):
    try:
        items = await asyncio.to_thread(get_cves)
        for cve in items or []:
            cve_id = str(cve.get("id", ""))
            score_raw = cve.get("score")
            try:
                score = float(score_raw)
            except (TypeError, ValueError):
                continue
            if not cve_id or score < 9.0:
                continue
            if _is_seen("critical_cve", cve_id):
                continue
            # First encounter is recorded without broadcasting to avoid a startup alert storm.
            _mark_seen("critical_cve", cve_id)
            description = html.escape(str(cve.get("description", "No description available"))[:700])
            link = html.escape(str(cve.get("link", "")), quote=True)
            message = f"🚨 <b>Critical CVE Alert (CVSS {score:.1f})</b>\n\n<b>{html.escape(cve_id)}</b>\n{description}\n\n<a href='{link}'>View CVE details</a>"
            await _broadcast(app, "Critical CVE", cve_id, message)
    except Exception:
        LOG.exception("Critical CVE monitor failed")


async def _kev_job(app: Application):
    try:
        response = await asyncio.to_thread(httpx.get, KEV_URL, timeout=20)
        response.raise_for_status()
        data = response.json()
        vulnerabilities = data.get("vulnerabilities", [])
        for item in vulnerabilities:
            cve_id = str(item.get("cveID", ""))
            if not cve_id or _is_seen("kev", cve_id):
                continue
            _mark_seen("kev", cve_id)
            title = html.escape(str(item.get("vulnerabilityName", cve_id)))
            vendor = html.escape(str(item.get("vendorProject", "Unknown")))
            product = html.escape(str(item.get("product", "Unknown")))
            due = html.escape(str(item.get("dueDate", "N/A")))
            message = (f"⚠️ <b>New CISA KEV Catalog Entry</b>\n\n<b>{html.escape(cve_id)}</b> — {title}\n"
                       f"Vendor/Product: {vendor} / {product}\nDue date: {due}\n\n"
                       f"<a href='https://www.cisa.gov/known-exploited-vulnerabilities-catalog'>CISA KEV Catalog</a>")
            await _broadcast(app, "CISA KEV", cve_id, message)
    except Exception:
        LOG.exception("CISA KEV monitor failed")


async def _daily_briefing_job(app: Application):
    for chat_id in _subscriber_ids():
        try:
            # Build content using the same data sources as the on-demand command.
            articles = await asyncio.to_thread(get_all_news, 5)
            cves = await asyncio.to_thread(get_cves)
            today = datetime.now(IST).strftime("%d %b %Y")
            lines = [f"🛡️ <b>ThreatScope Daily Briefing — {today}</b>", "", "<b>Top news</b>"]
            for article in (articles or [])[:5]:
                title = html.escape(str(article.get("title", "Untitled")))
                link = html.escape(str(article.get("link", "")), quote=True)
                lines.append(f"• <a href='{link}'>{title}</a>")
            lines.append("\n<b>Recent CVEs</b>")
            for cve in (cves or [])[:3]:
                cid = html.escape(str(cve.get("id", "CVE")))
                severity = html.escape(str(cve.get("severity", "Unknown")))
                link = html.escape(str(cve.get("link", "")), quote=True)
                lines.append(f"• <a href='{link}'>{cid}</a> — {severity}")
            await app.bot.send_message(chat_id, "\n".join(lines)[:4000], parse_mode="HTML", disable_web_page_preview=True)
        except Exception:
            LOG.exception("Daily briefing send failed for %s", chat_id)


async def _daily_threat_job(app: Application):
    day = datetime.now(IST).timetuple().tm_yday
    name, description = THREATS[(day - 1) % len(THREATS)]
    message = f"🛡️ <b>Threat of the Day</b>\n\n<b>{html.escape(name)}</b>\n{html.escape(description)}"
    for chat_id in _subscriber_ids():
        try:
            await app.bot.send_message(chat_id, message, parse_mode="HTML")
        except Exception:
            LOG.exception("Threat of the day send failed for %s", chat_id)


async def _seed_seen(app: Application):
    # Seed existing CVEs/KEVs at first run so only subsequent additions alert.
    try:
        items = await asyncio.to_thread(get_cves)
        for item in items or []:
            _mark_seen("critical_cve", item.get("id", ""))
    except Exception:
        LOG.exception("CVE baseline seed failed")
    try:
        response = await asyncio.to_thread(httpx.get, KEV_URL, timeout=20)
        response.raise_for_status()
        for item in response.json().get("vulnerabilities", []):
            _mark_seen("kev", item.get("cveID", ""))
    except Exception:
        LOG.exception("KEV baseline seed failed")


async def intelligence_post_init(app: Application):
    global _scheduler
    await _seed_seen(app)
    _scheduler = AsyncIOScheduler(timezone=IST)
    _scheduler.add_job(_critical_cve_job, "interval", hours=1, args=[app], id="critical_cve", max_instances=1, coalesce=True)
    _scheduler.add_job(_kev_job, "interval", minutes=30, args=[app], id="cisa_kev", max_instances=1, coalesce=True)
    _scheduler.add_job(_daily_briefing_job, "cron", hour=9, minute=0, args=[app], id="daily_briefing", max_instances=1)
    _scheduler.add_job(_daily_threat_job, "cron", hour=9, minute=10, args=[app], id="daily_threat", max_instances=1)
    _scheduler.start()
    LOG.info("ThreatScope intelligence scheduler started (IST).")


async def intelligence_post_shutdown(app: Application):
    global _scheduler
    if _scheduler and _scheduler.running:
        _scheduler.shutdown(wait=False)
    _scheduler = None
