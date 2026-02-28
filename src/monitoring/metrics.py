"""Metrics collection for Feynman Bot.

Collects:
- Lessons sent (total, by type)
- Errors (by category)
- Response times (LLM, DB)
- Bot commands usage

Metrics are logged periodically and can be exposed via health endpoint.
"""
import logging
import time
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from threading import Lock
from typing import Optional

log = logging.getLogger(__name__)


@dataclass
class MetricsSnapshot:
    """Point-in-time metrics snapshot."""
    timestamp: str
    lessons_sent_total: int
    lessons_sent_by_type: dict
    errors_total: int
    errors_by_category: dict
    llm_avg_response_ms: float
    db_avg_response_ms: float
    bot_commands_total: int
    bot_commands_by_type: dict
    uptime_seconds: float


class MetricsCollector:
    """Thread-safe metrics collector."""

    def __init__(self):
        self._lock = Lock()
        self._start_time = time.time()

        # Counters
        self._lessons_sent = defaultdict(int)
        self._errors = defaultdict(int)
        self._bot_commands = defaultdict(int)

        # Response times (for calculating averages)
        self._llm_times: list[float] = []
        self._db_times: list[float] = []

        # Max samples to keep for averaging
        self._max_samples = 1000

    def record_lesson_sent(self, lesson_type: str):
        """Record a lesson was sent to user."""
        with self._lock:
            self._lessons_sent[lesson_type] += 1
            self._lessons_sent["__total__"] += 1

    def record_error(self, category: str):
        """Record an error occurred."""
        with self._lock:
            self._errors[category] += 1
            self._errors["__total__"] += 1

    def record_llm_response(self, duration_ms: float):
        """Record LLM API response time."""
        with self._lock:
            self._llm_times.append(duration_ms)
            if len(self._llm_times) > self._max_samples:
                self._llm_times = self._llm_times[-self._max_samples:]

    def record_db_response(self, duration_ms: float):
        """Record DB query response time."""
        with self._lock:
            self._db_times.append(duration_ms)
            if len(self._db_times) > self._max_samples:
                self._db_times = self._db_times[-self._max_samples:]

    def record_bot_command(self, command: str):
        """Record a bot command was executed."""
        with self._lock:
            self._bot_commands[command] += 1
            self._bot_commands["__total__"] += 1

    def get_snapshot(self) -> MetricsSnapshot:
        """Get current metrics snapshot."""
        with self._lock:
            uptime = time.time() - self._start_time

            llm_avg = (
                sum(self._llm_times) / len(self._llm_times)
                if self._llm_times else 0.0
            )
            db_avg = (
                sum(self._db_times) / len(self._db_times)
                if self._db_times else 0.0
            )

            return MetricsSnapshot(
                timestamp=datetime.now().isoformat(),
                lessons_sent_total=self._lessons_sent.get("__total__", 0),
                lessons_sent_by_type={
                    k: v for k, v in self._lessons_sent.items()
                    if k != "__total__"
                },
                errors_total=self._errors.get("__total__", 0),
                errors_by_category={
                    k: v for k, v in self._errors.items()
                    if k != "__total__"
                },
                llm_avg_response_ms=round(llm_avg, 2),
                db_avg_response_ms=round(db_avg, 2),
                bot_commands_total=self._bot_commands.get("__total__", 0),
                bot_commands_by_type={
                    k: v for k, v in self._bot_commands.items()
                    if k != "__total__"
                },
                uptime_seconds=round(uptime, 2),
            )

    def log_summary(self):
        """Log current metrics summary."""
        snap = self.get_snapshot()
        log.info(
            "📊 Metrics: lessons=%d errors=%d llm_avg=%.0fms db_avg=%.0fms uptime=%.0fs",
            snap.lessons_sent_total,
            snap.errors_total,
            snap.llm_avg_response_ms,
            snap.db_avg_response_ms,
            snap.uptime_seconds,
        )

    def reset(self):
        """Reset all metrics (for testing)."""
        with self._lock:
            self._lessons_sent.clear()
            self._errors.clear()
            self._bot_commands.clear()
            self._llm_times.clear()
            self._db_times.clear()
            self._start_time = time.time()


# Global metrics instance
metrics = MetricsCollector()


def record_llm_latency(func):
    """Decorator to record LLM call latency."""
    import asyncio
    import functools

    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = await func(*args, **kwargs)
            return result
        finally:
            duration_ms = (time.time() - start) * 1000
            metrics.record_llm_response(duration_ms)

    @functools.wraps(func)
    def sync_wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            duration_ms = (time.time() - start) * 1000
            metrics.record_llm_response(duration_ms)

    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    return sync_wrapper
