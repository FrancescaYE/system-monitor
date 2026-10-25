from datetime import datetime
import psutil
import socket


#DEFINIR LA CLASSE DU SERVEUR
class ServerMonitor:
 def __init__(self, server_name, cpu_usage, memory_usage, disk_usage):
  self.server_name = server_name
  self.cpu_usage = cpu_usage
  self.memory_usage = memory_usage
  self.disk_usage = disk_usage



#FONCTION DE COLLECTE : LA DATE + INFOS SERVEURS(NOM,CPU,MEMOIRE,DISQUE)
#la date
def get_formatted_date():
 now = datetime.now()
 formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
 return formatted_date

#nom
def get_server_name():
 try:
  server_name = socket.gethostname()
  return server_name
 except OSError:
  print("Error: Unable to retrieve the server's name.")
  return None

# cpu
def get_cpu_usage():
 try:
  cpu_usage = psutil.cpu_percent(interval=1)
  return cpu_usage
 except OSError:
  print("Error: Unable to retrieve CPU usage.")
  return None

#memoire
def get_memory_usage():
 try:
  memory_usage = psutil.virtual_memory().percent
  return memory_usage
 except OSError:
  print("Error: Unable to retrieve memory usage.")
  return None

#espace disque
def get_disk_usage():
 try:
  disk_usage = psutil.disk_usage("/").percent
  return disk_usage
 except OSError:
  print("Error: Unable to retrieve disk usage.")
  return None

