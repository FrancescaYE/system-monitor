# CloudOps Monitor

CloudOps Monitor est une application de supervision développée en Python. Elle permet de collecter et d’afficher des métriques système, de surveiller l’état des serveurs, de vérifier la disponibilité des services web et de consulter l’historique des opérations de supervision à travers une interface web.

Le projet combine la supervision système, la persistance des données, l’analyse des résultats et la gestion des alertes à partir des journaux, au sein d’une application web développée avec Flask.

## Fonctionnalités

* Métriques système : collecte de l’utilisation du processeur (CPU), de la mémoire et du disque.
* Surveillance de l’état des serveurs : évaluation de leur état de santé à partir des résultats de supervision.
* Vérification des services web : contrôle de leur disponibilité et enregistrement des réponses HTTP.
* Historique de supervision : stockage des résultats dans une base de données SQLite.
* Tableau de bord analytique : affichage de statistiques et filtrage des résultats par période et par état de santé.
* Journaux et alertes : consultation des rapports de supervision et filtrage des alertes et des erreurs liées aux services web.
* Interface web : tableau de bord développé avec Flask, HTML, CSS et JavaScript.

## Approche de conception

Ce projet utilise des modèles HTML et le framework d’interface Tabler afin de proposer une interface web claire et fonctionnelle.

J’ai choisi cette approche pour me concentrer principalement sur le développement backend, notamment la collecte des métriques système, la surveillance de l’état des serveurs, les opérations sur la base de données, l’analyse des résultats et la gestion des journaux, tout en proposant une application web utilisable.

Cette approche m’a permis de privilégier la logique de supervision et les fonctionnalités liées aux systèmes et à l’infrastructure, plutôt que de développer une interface frontend entièrement à partir de zéro.

## Technologies utilisées

* Python : logique principale de l’application et opérations de supervision.
* Flask : framework web utilisé pour gérer l’application et ses routes.
* SQLite : stockage persistant de l’historique de supervision.
* psutil : collecte des métriques système.
* Requests : envoi de requêtes HTTP pour vérifier la disponibilité des services web.
* HTML, CSS et JavaScript : technologies utilisées pour l’interface web.
* Tabler : framework d’interface utilisé pour construire la structure et les composants du tableau de bord.
* Git : gestion des versions du code.
* Linux (Ubuntu/WSL) : environnement de développement.

## Structure du projet

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

## Principaux composants

* app.py : définit l’application Flask et les routes web.
* config.py : gère la configuration de l’application.
* database/ : contient les fonctionnalités d’initialisation de la base de données, de stockage des métriques et de récupération de l’historique.
* monitoring/ : regroupe la logique de supervision, la collecte des métriques, les contrôles d’état, les rapports, les journaux et les analyses.
* templates/ : contient les modèles HTML utilisés pour afficher les pages web.
* static/ : contient les ressources CSS et JavaScript de l’interface.
* requirements.txt : répertorie les dépendances Python nécessaires à l’application.

## Installation et utilisation

### Prérequis

* Python 3
* Git
* Un environnement Linux ou Ubuntu via WSL

### 1. Cloner le dépôt

```bash
git clone <repository-url>
cd python-cloudops-monitor
```

Remplacez `<repository-url>` par l’URL réelle de votre dépôt GitHub une fois celui-ci créé.

### 2. Créer un environnement virtuel

```bash
python3 -m venv .venv
```

### 3. Activer l’environnement virtuel

```bash
source .venv/bin/activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 5. Démarrer l’application

```bash
flask --app app run
```

### 6. Accéder au tableau de bord

Ouvrez l’adresse suivante dans votre navigateur :

http://127.0.0.1:5000

L’application donne accès au tableau de bord, à la page d’analyse et d’historique, ainsi qu’à la page des journaux et des alertes.
