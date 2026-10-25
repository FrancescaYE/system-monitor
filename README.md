# CloudOps Monitor

CloudOps Monitor is a Python-based monitoring application designed to collect and display system metrics, monitor server health, check web service availability, and provide historical monitoring data through a web interface.

The project combines system monitoring, data persistence, analytics, and log-based alerts in a Flask web application.

## Features

* System Metrics: Collects CPU, memory, and disk usage.
* Server Health Monitoring: Evaluates server health based on monitoring results.
* Web Service Checks: Checks web service availability and records HTTP responses.
* Monitoring History: Stores monitoring results in an SQLite database.
* Analytics Dashboard: Displays monitoring statistics and supports filtering by period and health status.
* Logs and Alerts: Displays monitoring reports and allows filtering of alerts and web service errors.
* Web Interface: Provides a dashboard built with Flask, HTML, CSS, and JavaScript.

## Design Approach

This project uses HTML templates and the Tabler UI framework to provide a clean and functional web interface.

I chose this approach to focus primarily on backend development, including system metrics collection, server health monitoring, database operations, analytics, and log management, while still delivering a usable web application.

This allowed me to prioritize the core monitoring logic and infrastructure-related functionality rather than building a frontend interface from scratch.

## Technologies Used

* Python: Core application logic and monitoring operations.
* Flask: Web application framework and routing.
* SQLite: Persistent storage for monitoring history.
* psutil: System metrics collection.
* Requests: HTTP requests for web service availability checks.
* HTML, CSS, and JavaScript: Web interface.
* Tabler: UI framework used to build the dashboard layout and components.
* Git: Version control.
* Linux (Ubuntu/WSL): Development environment.

## Project Structure

```text
python-cloudops-monitor/
├── app.py
├── config.py
├── requirements.txt
├── database/
│   ├── __init__.py
│   ├── db.py
│   └── schema.sql
├── monitoring/
│   ├── __init__.py
│   ├── analytics.py
│   ├── health.py
│   ├── logs.py
│   ├── metrics.py
│   ├── reports.py
│   ├── service.py
│   └── web_checks.py
├── static/
│   ├── css/
│   └── js/
└── templates/
    ├── base.html
    ├── index.html
    ├── analytics.html
    └── logs.html
```

## Main Components

* app.py: Defines the Flask application and web routes.
* config.py: Manages application configuration.
* database/: Handles database initialization, metric storage, and history retrieval.
* monitoring/: Contains the monitoring logic, metrics collection, health checks, reports, logs, and analytics.
* templates/: Contains the HTML templates used to render the web pages.
* static/: Contains the CSS and JavaScript resources used by the interface.
* requirements.txt: Lists the Python dependencies required to run the application.

## Installation and Usage

### Prerequisites

* Python 3
* Git
* A Linux environment or Ubuntu through WSL

### 1. Clone the Repository

```bash
git clone <repository-url>
cd python-cloudops-monitor
```

Replace `<repository-url>` with the URL of your GitHub repository.

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the Application

```bash
flask --app app run
```

### 6. Open the Dashboard

Open the following address in your browser:

http://127.0.0.1:5000

The application provides access to the Dashboard, Analytics & History, and Logs & Alerts pages.
