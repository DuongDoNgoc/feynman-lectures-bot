"""Health check endpoints for Feynman Bot.

Provides:
- HTTP health check endpoint (optional, for monitoring systems)
- Database health check
- LLM API health check

Run standalone: python -m src.monitoring.health
"""
import asyncio
import logging
import os
import sqlite3
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

log = logging.getLogger(__name__)


@dataclass
class HealthStatus:
    """Health check result."""
    healthy: bool
    component: str
    message: str
    latency_ms: Optional[float] = None
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()

    def to_dict(self) -> dict:
        return {
            "healthy": self.healthy,
            "component": self.component,
            "message": self.message,
            "latency_ms": self.latency_ms,
            "timestamp": self.timestamp,
        }


async def check_database(db_path: str) -> HealthStatus:
    """Check database connectivity and basic integrity."""
    import time

    start = time.time()
    try:
        # Use sync sqlite3 for simple health check
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Check tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]

        required = {"lessons", "sections", "chapters", "user_progress"}
        missing = required - set(tables)

        conn.close()

        latency = (time.time() - start) * 1000

        if missing:
            return HealthStatus(
                healthy=False,
                component="database",
                message=f"Missing tables: {missing}",
                latency_ms=round(latency, 2),
            )

        return HealthStatus(
            healthy=True,
            component="database",
            message=f"OK ({len(tables)} tables)",
            latency_ms=round(latency, 2),
        )

    except Exception as e:
        latency = (time.time() - start) * 1000
        return HealthStatus(
            healthy=False,
            component="database",
            message=f"Error: {e}",
            latency_ms=round(latency, 2),
        )


async def check_llm_api(config: dict) -> HealthStatus:
    """Check LLM API connectivity (lightweight ping)."""
    import time
    import os

    start = time.time()
    provider = config.get("qa", {}).get("provider", "deepseek")
    api_key = os.environ.get("DEEPSEEK_API_KEY" if provider == "deepseek" else "ANTHROPIC_API_KEY", "")

    if not api_key:
        return HealthStatus(
            healthy=False,
            component="llm_api",
            message="API key not configured",
        )

    try:
        # Simple API reachability check
        import aiohttp

        if provider == "deepseek":
            url = "https://api.deepseek.com/v1/models"
            headers = {"Authorization": f"Bearer {api_key}"}
        else:
            url = "https://api.anthropic.com/v1/models"
            headers = {"x-api-key": api_key}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                latency = (time.time() - start) * 1000

                if resp.status in (200, 403):  # 403 = auth OK, just no permission for this endpoint
                    return HealthStatus(
                        healthy=True,
                        component="llm_api",
                        message=f"OK ({provider})",
                        latency_ms=round(latency, 2),
                    )
                else:
                    return HealthStatus(
                        healthy=False,
                        component="llm_api",
                        message=f"HTTP {resp.status}",
                        latency_ms=round(latency, 2),
                    )

    except asyncio.TimeoutError:
        latency = (time.time() - start) * 1000
        return HealthStatus(
            healthy=False,
            component="llm_api",
            message="Timeout",
            latency_ms=round(latency, 2),
        )
    except Exception as e:
        latency = (time.time() - start) * 1000
        return HealthStatus(
            healthy=False,
            component="llm_api",
            message=f"Error: {e}",
            latency_ms=round(latency, 2),
        )


async def check_telegram_api(config: dict) -> HealthStatus:
    """Check Telegram Bot API connectivity."""
    import time
    import aiohttp

    start = time.time()
    token = config.get("telegram", {}).get("bot_token", "")

    if not token or token.startswith("${"):
        return HealthStatus(
            healthy=False,
            component="telegram_api",
            message="Bot token not configured",
        )

    try:
        url = f"https://api.telegram.org/bot{token}/getMe"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                latency = (time.time() - start) * 1000

                if resp.status == 200:
                    data = await resp.json()
                    if data.get("ok"):
                        bot_name = data.get("result", {}).get("username", "unknown")
                        return HealthStatus(
                            healthy=True,
                            component="telegram_api",
                            message=f"OK (@{bot_name})",
                            latency_ms=round(latency, 2),
                        )

                return HealthStatus(
                    healthy=False,
                    component="telegram_api",
                    message=f"HTTP {resp.status}",
                    latency_ms=round(latency, 2),
                )

    except Exception as e:
        latency = (time.time() - start) * 1000
        return HealthStatus(
            healthy=False,
            component="telegram_api",
            message=f"Error: {e}",
            latency_ms=round(latency, 2),
        )


async def full_health_check(config: dict) -> dict:
    """Run all health checks and return summary."""
    results = await asyncio.gather(
        check_database(config.get("database", {}).get("path", "data/feynman.db")),
        check_llm_api(config),
        check_telegram_api(config),
    )

    all_healthy = all(r.healthy for r in results)

    return {
        "status": "healthy" if all_healthy else "unhealthy",
        "timestamp": datetime.now().isoformat(),
        "checks": [r.to_dict() for r in results],
    }


def print_health_report(report: dict):
    """Print human-readable health report."""
    print(f"\n{'='*50}")
    print(f"Health Check Report: {report['status'].upper()}")
    print(f"Timestamp: {report['timestamp']}")
    print(f"{'='*50}")

    for check in report["checks"]:
        status = "✅" if check["healthy"] else "❌"
        latency = f" ({check['latency_ms']:.0f}ms)" if check.get("latency_ms") else ""
        print(f"{status} {check['component']}: {check['message']}{latency}")

    print(f"{'='*50}\n")


async def main():
    """Run health checks from command line."""
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

    from src.utils import load_config, setup_logging

    config = load_config()
    setup_logging({"logging": {"level": "WARNING", "file": None}})

    report = await full_health_check(config)
    print_health_report(report)

    # Exit with error code if unhealthy
    return 0 if report["status"] == "healthy" else 1


if __name__ == "__main__":
    exit(asyncio.run(main()))
