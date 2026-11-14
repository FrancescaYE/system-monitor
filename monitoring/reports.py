# CONSTRUIRE LE RÉSUMÉ DES ALERTES
def build_alert_summary(cpu_status, memory_status,
                        disk_status, health_status, status_code):

    alerts = []

    if "WARNING" in cpu_status:
        alerts.append(cpu_status)

    if "WARNING" in memory_status:
        alerts.append(memory_status)

    if "WARNING" in disk_status:
        alerts.append(disk_status)

    if health_status == "UNKNOWN":
        alerts.append("Server health is unknown")

    if status_code is None:
        alerts.append("Web service is unavailable")
    elif status_code < 200 or status_code >= 300:
        alerts.append(f"Web service returned HTTP {status_code}")

    if not alerts:
        return "No warnings found."

    return "\n".join(alerts)  


# CONSTRUIRE LE RAPPORT DE SURVEILLANCE
def build_report(date, server, cpu_status, memory_status,
                 disk_status, health_status, web_url,
                 status_code, web_status, alert_summary):

    report = f"""
==================================================
                 SYSTEMMONITOR
==================================================
Monitoring date: {date}
Server name: {server.server_name if server.server_name is not None else "Unavailable"}

---------------- SYSTEM METRICS -----------------
CPU usage: {server.cpu_usage if server.cpu_usage is not None else "Unavailable"}{"%" if server.cpu_usage is not None else ""}
CPU status: {cpu_status}
Memory usage: {server.memory_usage if server.memory_usage is not None else "Unavailable"}{"%" if server.memory_usage is not None else ""}
Memory status: {memory_status}
Disk usage: {server.disk_usage if server.disk_usage is not None else "Unavailable"}{"%" if server.disk_usage is not None else ""}
Disk status: {disk_status}

---------------- SERVER HEALTH ------------------
Server health: {health_status}

---------------- WEB SERVICE --------------------
URL: {web_url}
HTTP status code: {status_code if status_code is not None else "Unavailable"}
Web service status: {web_status}

---------------- ALERT SUMMARY -------------------
{alert_summary}
==================================================
"""
    return report