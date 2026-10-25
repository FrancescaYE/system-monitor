import os

#LES VARIABLES SEUILS
CPU_THRESHOLD = int(os.getenv("CPU_THRESHOLD", "80"))
MEMORY_THRESHOLD = int(os.getenv("MEMORY_THRESHOLD", "80"))
DISK_THRESHOLD = int(os.getenv("DISK_THRESHOLD", "80"))


#LES FONCTIONS D'ANALYSE(CPU,MEMOIRE,DISQUE,ETAT GLOBAL)
#Analyse cpu
def check_cpu(cpu_usage):
 if cpu_usage is None:
  return "CPU usage unavailable"
 elif cpu_usage >= CPU_THRESHOLD:
  return "WARNING: High CPU usage!"
 else:
  return "CPU usage is normal"

#Analyse mémoire
def check_memory(memory_usage):
 if memory_usage is None:
  return "Memory usage unavailable"
 elif memory_usage >= MEMORY_THRESHOLD:
  return "WARNING: High memory usage!"
 else:
  return "Memory usage is normal"

#Analyse disque
def check_disk(disk_usage):
 if disk_usage is None:
  return "Disk usage unavailable"
 elif disk_usage >= DISK_THRESHOLD:
  return "WARNING: High disk usage!"
 else:
   return "Disk usage is normal"

#Analyse global
def check_server_health(cpu_usage, memory_usage, disk_usage):
 if cpu_usage is None or memory_usage is None or disk_usage is None:
  return "UNKNOWN"
 elif (cpu_usage < CPU_THRESHOLD and memory_usage < MEMORY_THRESHOLD and disk_usage < DISK_THRESHOLD):
  return "HEALTHY"
 else:
  return "WARNING"


