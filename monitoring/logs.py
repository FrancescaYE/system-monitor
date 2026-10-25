#FONCTIONS DE GESTION DES LOGS
#enregistrement du rapport
def write_logs(report):
    try:
        with open("cloudops.log", "a") as fichier:
            fichier.write(report + "\n")
    except OSError:
        print("Error: Failed to write to the log file.")

#lecture et analyse de l'historique
def read_monitoring_logs():
 try:
  with open("cloudops.log", "r") as fichier:
   content = fichier.read()
   if not content:
    print("The log file is empty")
   else:
    #afficher les alertes
    compteur = 0
    for ligne in content.splitlines():
     if "WARNING: High CPU usage!" in ligne:
      print("CPU alert: ", ligne)
     elif "WARNING: High memory usage!" in ligne:
      print("Memory alert: ", ligne)
     elif "WARNING: High disk usage!" in ligne:
      print("Disk alert:", ligne)
     elif "WARNING" in ligne:
      print("Health alert:", ligne)

     if "WARNING" in ligne:
      compteur += 1

    if compteur == 0:
     print("No warnings found.")


 except FileNotFoundError:
  print("Error: Log file not found.")

def get_monitoring_logs():
  try:
    with open("cloudops.log", "r") as fichier:
     content = fichier.read().strip()

    if not content:
         return []
    reports = content.split("Monitoring date:")[1:]
    return [
     "Monitoring date:" + report.split(
      "=================================================="
     )[0].strip()
            + "\n=================================================="
            for report in reversed(reports)
            if report.strip()
        ]
  except (FileNotFoundError, OSError):
    return []