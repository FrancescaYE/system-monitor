import requests


#FONCTIONS POUR VERIFICATION ET INTERPRETATION WEB
#verification 
def check_web_service(url):
 try:
  response = requests.get(url, timeout=5)
  return response.status_code
 except requests.exceptions.RequestException:
  return None
 
#Interpretation du status web
def interpret_web_status(status_code):
    if status_code is None:
        return "Service unavailable"
    elif 200 <= status_code < 300:
        return "Web service is responding normally"
    elif status_code == 404:
        return "Resource not found"
    elif 400 <= status_code < 500:
        return "Client or request error"
    elif 500 <= status_code < 600:
        return "Server error"
    else:
        return "Unexpected HTTP status" 
    