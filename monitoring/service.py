#LES IMPORTS

#imports databse
from database.db import (
    initialize_database,
    save_metrics
)

#imports pour collecter valeurs
from monitoring.metrics import (
    ServerMonitor,
    get_formatted_date,
    get_server_name,
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
)

#imports analyse du systeme
from monitoring.health import (
    check_cpu,
    check_memory,
    check_disk,
    check_server_health,
)

#imports pour analyse du service web
from monitoring.web_checks import (
    check_web_service,
    interpret_web_status,
)

#imports pour construction alerte, rapport
from monitoring.reports import (
    build_alert_summary,
    build_report,
)

#imports pour enregistrements et analyse logs
from monitoring.logs import write_logs


#fonction pour coordonner le monitoring
def run_monitoring(web_url="https://example.com"):
    # Initialiser la base de données
    initialize_database()

    # Collecter les métriques
    date = get_formatted_date()
    server_name = get_server_name()
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()

    # Créer l'objet représentant le serveur
    server = ServerMonitor(
        server_name,
        cpu_usage,
        memory_usage,
        disk_usage,
    )

    # Analyser les métriques
    cpu_status = check_cpu(server.cpu_usage)
    memory_status = check_memory(server.memory_usage)
    disk_status = check_disk(server.disk_usage)

    health_status = check_server_health(
        server.cpu_usage,
        server.memory_usage,
        server.disk_usage,
    )

    # Vérifier le service web
    status_code = check_web_service(web_url)
    web_status = interpret_web_status(status_code)

    # Construire le résumé des alertes
    alert_summary = build_alert_summary(
        cpu_status,
        memory_status,
        disk_status,
        health_status,
        status_code,
    )

    # Construire le rapport
    report = build_report(
        date,
        server,
        cpu_status,
        memory_status,
        disk_status,
        health_status,
        web_url,
        status_code,
        web_status,
        alert_summary,
    )

    # Enregistrer les résultats
    write_logs(report)
    save_metrics(
    date,
    server,
    cpu_status,
    memory_status,
    disk_status,
    health_status,
    web_url,
    status_code,
    web_status,
)

    # Retourner les résultats pour le terminal ou Flask
    return {
        "date": date,
        "server": server,
        "cpu_status": cpu_status,
        "memory_status": memory_status,
        "disk_status": disk_status,
        "health_status": health_status,
        "web_url": web_url,
        "status_code": status_code,
        "web_status": web_status,
        "alert_summary": alert_summary,
        "report": report,
    }