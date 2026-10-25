import sqlite3
from contextlib import closing

#colonnes autorisees
ALLOWED_COLUMNS = ("cpu_usage", "memory_usage", "disk_usage")

#creation de la base
def initialize_database():
    try:
        with closing(sqlite3.connect("cloudops.db")) as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS monitoring_metrics(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    server_name TEXT,
                    cpu_usage REAL,
                    memory_usage REAL,
                    disk_usage REAL
                )
            """)

            # Colonnes supplémentaires à ajouter si nécessaire
            new_columns = {
                "cpu_status": "TEXT",
                "memory_status": "TEXT",
                "disk_status": "TEXT",
                "health_status": "TEXT",
                "web_url": "TEXT",
                "status_code": "INTEGER",
                "web_status": "TEXT",
            }

            # Récupérer les colonnes déjà présentes
            result = connection.execute(
                "PRAGMA table_info(monitoring_metrics)"
            )
            existing_columns = {
                column[1] for column in result.fetchall()
            }

            # Ajouter uniquement les colonnes manquantes
            for column_name, column_type in new_columns.items():
                if column_name not in existing_columns:
                    connection.execute(
                        f"ALTER TABLE monitoring_metrics "
                        f"ADD COLUMN {column_name} {column_type}"
                    )

            connection.commit()

    except sqlite3.Error as error:
        print(f"Erreur SQLite lors de l'initialisation : {error}")

#insertion dans la base
def save_metrics(
    date,
    server,
    cpu_status,
    memory_status,
    disk_status,
    health_status,
    web_url,
    status_code,
    web_status,
):
    try:
        with closing(sqlite3.connect("cloudops.db")) as connection:
            connection.execute("""
                INSERT INTO monitoring_metrics (
                    date,
                    server_name,
                    cpu_usage,
                    memory_usage,
                    disk_usage,
                    cpu_status,
                    memory_status,
                    disk_status,
                    health_status,
                    web_url,
                    status_code,
                    web_status
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                date,
                server.server_name,
                server.cpu_usage,
                server.memory_usage,
                server.disk_usage,
                cpu_status,
                memory_status,
                disk_status,
                health_status,
                web_url,
                status_code,
                web_status,
            ))
            connection.commit()

    except sqlite3.Error as error:
        print(f"Erreur SQLite lors de l'enregistrement : {error}")

#historique de la base
def get_monitoring_history():
    with closing(sqlite3.connect("cloudops.db")) as connection:
        result = connection.execute(
            "SELECT * FROM monitoring_metrics ORDER BY id DESC LIMIT 3"
        )
        records = result.fetchall()
    return records

def get_full_monitoring_history():
    with closing(sqlite3.connect("cloudops.db")) as connection:
        result = connection.execute(
            "SELECT * FROM monitoring_metrics ORDER BY id DESC"
        )
        records = result.fetchall()
    return records

#moyenne d'utilisation de la column(cpu, memory,disk)
def get_average_usage(column):
    if column not in ALLOWED_COLUMNS:
        raise ValueError(f"unauthorized column : {column}")
    with closing(sqlite3.connect("cloudops.db")) as connection:
        result = connection.execute(
            f"SELECT AVG({column}) FROM monitoring_metrics;"
        )
        average = result.fetchone()[0]
    return average

#plus grande valeur de la column(cpu, memory,disk)
def get_max_usage(column):
    if column not in ALLOWED_COLUMNS:
        raise ValueError(f"unauthorized column : {column}")
    with closing(sqlite3.connect("cloudops.db")) as connection:
        result = connection.execute(
            f"SELECT MAX({column}) FROM monitoring_metrics;"
        )
        max_value = result.fetchone()[0]
    return max_value

#plus petite valeur de la column(cpu, memory,disk)
def get_min_usage(column):
    if column not in ALLOWED_COLUMNS:
        raise ValueError(f"unauthorized column : {column}")
    with closing(sqlite3.connect("cloudops.db")) as connection:
        result = connection.execute(
            f"SELECT MIN({column}) FROM monitoring_metrics;"
        )
        min_value = result.fetchone()[0]
    return min_value