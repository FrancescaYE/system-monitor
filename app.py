from flask import (
    Flask,
    flash,
    render_template,
    redirect,
    url_for,
    request,
)
from config import Config
from database.db import get_monitoring_history
from monitoring.service import run_monitoring
from monitoring.analytics import (
    filter_monitoring_history,
    get_filtered_analytics,
    get_health_distribution,
)
from monitoring.logs import get_monitoring_logs

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
    history = get_monitoring_history()
    latest_record = history[0] if history else None
    return render_template(
        "index.html",
        latest_record=latest_record
    )

@app.route("/run-monitoring", methods=["POST"])
def trigger_monitoring():
    run_monitoring()
    flash("Monitoring completed successfully!")
    return redirect(url_for("home"))

@app.route("/analytics")
def analytics():
    period = request.args.get("period", "24h")
    health_status = request.args.get("health_status", "all")
    start_date = request.args.get("start_date") or None
    end_date = request.args.get("end_date") or None

    if period not in ("1h", "24h", "7d", "custom"):
        period = "24h"

    if health_status not in ("all", "HEALTHY", "WARNING", "UNKNOWN"):
        health_status = "all"

    history = filter_monitoring_history(
        period=period,
        health_status=health_status,
        start_date=start_date,
        end_date=end_date,
    )

    stats = get_filtered_analytics(history)
    health_distribution = get_health_distribution(history)


    return render_template(
        "analytics.html",
        history=history,
        stats=stats,
        period=period,
        health_status=health_status,
        start_date=start_date or "",
        end_date=end_date or "",
        health_distribution=health_distribution,
    )

@app.route("/logs")
def logs():
    logs_content = get_monitoring_logs()

    alert_filter = request.args.get("filter", "all")

    if alert_filter == "alerts":
        alert_keywords = (
            "WARNING: High CPU usage!",
            "WARNING: High memory usage!",
            "WARNING: High disk usage!",
            "Web service is unavailable",
            "Web service returned HTTP",
        )

        logs_content = [
            report for report in logs_content
            if any(keyword in report for keyword in alert_keywords)
        ]

    elif alert_filter == "web_errors":
        logs_content = [
            report for report in logs_content
            if (
                "Web service is unavailable" in report
                or "Web service returned HTTP" in report
            )
        ]

    return render_template(
        "logs.html",
        logs_content=logs_content,
        alert_filter=alert_filter,
    )