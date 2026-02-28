"""Monitoring module for Feynman Bot.

Provides:
- Metrics collection (lessons, errors, response times)
- Health check endpoints
"""
from src.monitoring.metrics import MetricsCollector, metrics, record_llm_latency
from src.monitoring.health import (
    HealthStatus,
    check_database,
    check_llm_api,
    check_telegram_api,
    full_health_check,
    print_health_report,
)

__all__ = [
    "MetricsCollector",
    "metrics",
    "record_llm_latency",
    "HealthStatus",
    "check_database",
    "check_llm_api",
    "check_telegram_api",
    "full_health_check",
    "print_health_report",
]
