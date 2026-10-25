from database.db import (
    get_average_usage,
    get_max_usage,
    get_min_usage,
)

from datetime import datetime, timedelta
from database.db import get_full_monitoring_history


def get_usage_analytics():
    metrics = ("cpu_usage", "memory_usage", "disk_usage")

    analytics = {}

    for metric in metrics:
        analytics[metric] = {
            "average": get_average_usage(metric),
            "maximum": get_max_usage(metric),
            "minimum": get_min_usage(metric),
        }
    return analytics


def filter_monitoring_history(
    period="24h",
    health_status="all",
    start_date=None,
    end_date=None,
):
    history = get_full_monitoring_history()
    now = datetime.now()

    period_limits = {
        "1h": now - timedelta(hours=1),
        "24h": now - timedelta(hours=24),
        "7d": now - timedelta(days=7),
    }

    filtered_history = []

    for record in history:
        try:
            record_date = datetime.strptime(
                record[1],
                "%d/%m/%Y %H:%M:%S",
            )
        except (ValueError, TypeError):
            continue

        if period in period_limits:
            if record_date < period_limits[period]:
                continue

        elif period == "custom":
            if start_date:
                start = datetime.strptime(start_date, "%Y-%m-%d")
                if record_date < start:
                    continue

            if end_date:
                end = datetime.strptime(
                    end_date, "%Y-%m-%d"
                ) + timedelta(days=1)

                if record_date >= end:
                    continue

        if health_status != "all":
            if record[9] != health_status:
                continue

        filtered_history.append(record)

    return filtered_history


def get_filtered_analytics(filtered_history):
    metrics = {
        "cpu_usage": 3,
        "memory_usage": 4,
        "disk_usage": 5,
    }

    analytics = {
        "total_measurements": len(filtered_history),
        "warning_count": sum(
            1 for record in filtered_history
            if record[9] == "WARNING"
        ),
    }

    for metric, index in metrics.items():
        values = [record[index] for record in filtered_history]

        analytics[metric] = {
            "average": sum(values) / len(values) if values else 0,
            "maximum": max(values) if values else 0,
            "minimum": min(values) if values else 0,
        }

    return analytics



def get_health_distribution(filtered_history):
    healthy_count = sum(
        1 for record in filtered_history
        if record[9] == "HEALTHY"
    )
    warning_count = sum(
        1 for record in filtered_history
        if record[9] == "WARNING"
    )
    health_distribution = {
        "HEALTHY": healthy_count,
        "WARNING": warning_count,
    }
    return health_distribution