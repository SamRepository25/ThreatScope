import logging
import time
import requests
from datetime import datetime

logger = logging.getLogger(__name__)

API_URL = (
    "https://services.nvd.nist.gov/rest/json/cves/2.0"
    "?resultsPerPage=10"
)

REQUEST_TIMEOUT = 8          # seconds, per attempt
MAX_ATTEMPTS = 3             # total attempts (1 initial + 2 retries)
BACKOFF_SCHEDULE = [1, 2]    # seconds to wait before retry 2 and retry 3
RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}
MAX_RETRY_AFTER = 5          # seconds; longer Retry-After values are not honored


def get_cves():
    """Fetch the latest CVEs from the NVD API."""

    data = None

    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            response = requests.get(API_URL, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            data = response.json()
            break

        except requests.exceptions.HTTPError as e:
            status = e.response.status_code if e.response is not None else None

            if status not in RETRYABLE_STATUS_CODES:
                logger.warning(
                    "NVD request failed with non-retryable HTTP %s "
                    "(attempt %d/%d). Not retrying.",
                    status, attempt, MAX_ATTEMPTS,
                )
                return []

            wait = None

            if status == 429:
                retry_after_header = (
                    e.response.headers.get("Retry-After")
                    if e.response is not None else None
                )

                if retry_after_header is not None:
                    try:
                        retry_after = float(retry_after_header)
                    except ValueError:
                        retry_after = None

                    if retry_after is not None and retry_after > MAX_RETRY_AFTER:
                        logger.warning(
                            "NVD requested a %.0fs wait via Retry-After, "
                            "exceeding the %ds cap. Aborting without retry "
                            "(attempt %d/%d).",
                            retry_after, MAX_RETRY_AFTER, attempt, MAX_ATTEMPTS,
                        )
                        return []

                    wait = retry_after

            if wait is None and attempt <= len(BACKOFF_SCHEDULE):
                wait = BACKOFF_SCHEDULE[attempt - 1]

            logger.warning(
                "NVD request failed with HTTP %s (attempt %d/%d).",
                status, attempt, MAX_ATTEMPTS,
            )

            if attempt < MAX_ATTEMPTS and wait is not None:
                logger.info("Retrying CVE fetch in %.0fs...", wait)
                time.sleep(wait)
                continue

            return []

        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            logger.warning(
                "NVD request failed with %s (attempt %d/%d).",
                type(e).__name__, attempt, MAX_ATTEMPTS,
            )

            if attempt < MAX_ATTEMPTS:
                wait = BACKOFF_SCHEDULE[attempt - 1]
                logger.info("Retrying CVE fetch in %.0fs...", wait)
                time.sleep(wait)
                continue

            return []

        except Exception as e:
            # JSON decoding errors or any other unexpected/programming
            # error. Not retried.
            logger.error("Unexpected error fetching CVEs: %s", e, exc_info=True)
            return []

    if data is None:
        return []

    try:
        results = []

        for index, item in enumerate(data.get("vulnerabilities", [])):

            try:
                cve = item["cve"]

                cve_id = cve["id"]

                description = cve["descriptions"][0]["value"]

                published = cve["published"]

                published = datetime.fromisoformat(
                    published.replace("Z", "+00:00")
                ).strftime("%d %b %Y")

                score = "N/A"
                severity = "UNKNOWN"

                metrics = cve.get("metrics", {})

                if "cvssMetricV31" in metrics:
                    metric = metrics["cvssMetricV31"][0]
                    score = metric["cvssData"]["baseScore"]
                    severity = metric["cvssData"]["baseSeverity"]

                elif "cvssMetricV30" in metrics:
                    metric = metrics["cvssMetricV30"][0]
                    score = metric["cvssData"]["baseScore"]
                    severity = metric["cvssData"]["baseSeverity"]

                elif "cvssMetricV2" in metrics:
                    metric = metrics["cvssMetricV2"][0]
                    score = metric["cvssData"]["baseScore"]
                    severity = metric["baseSeverity"]

                results.append(
                    {
                        "id": cve_id,
                        "description": description,
                        "published": published,
                        "severity": severity,
                        "score": score,
                        "link": f"https://nvd.nist.gov/vuln/detail/{cve_id}",
                    }
                )

            except Exception:
                entry_id = item.get("cve", {}).get("id", "unknown ID")
                logger.warning(
                    "Skipping malformed CVE entry at index %d (id: %s)",
                    index,
                    entry_id,
                    exc_info=True,
                )
                continue

        return results

    except Exception as e:
        logger.error("Unexpected error processing CVE data: %s", e, exc_info=True)
        return []