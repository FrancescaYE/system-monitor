CREATE TABLE IF NOT EXISTS monitoring_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    server_name TEXT,
    cpu_usage REAL,
    memory_usage REAL,
    disk_usage REAL,
    cpu_status TEXT,
    memory_status TEXT,
    disk_status TEXT,
    health_status TEXT,
    web_url TEXT,
    status_code INTEGER,
    web_status TEXT
);
