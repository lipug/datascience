''' 
Module utilitaire pour la lecture des fichiers depuis le web et l'écriture en local
'''
import requests
drive_path=''
DEBUG = False

def read_from_web(url, local):
  '''
  Procedure de lecture une url et la sauvegarder en local

  :param url: l'url à lire
  :param local: path du fichier en local
  '''
  if DEBUG: print(url,local)
  response = requests.get(url)
  response.raise_for_status()    # Check that the request was successful
  with open(local, "wb") as f:
    f.write(response.content)

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition
def get_local_form_response(response):
  '''
  trouver le nom du fichier en local en fonction de la réponse get
  Si c'est un attachement : le nom de l'attachement
  Sinon la dernière partie de l'url

  :param response: une réponse get
  '''
  attach = response.headers.get('Content-Disposition')
  url = response.url
  if (DEBUG): print(attach)
  if (attach and "filename=" in attach):
    local = attach.split("filename=")[-1]
  else:
    local = url.split("/")[-1]
  return local

# Version améliorée où on trouve le path du fichier local 
# en fonction de l'url et de son header (au cas d'un attachement)
def read_from_url(url, path=""):
  '''
  Procedure de lecture une url et la sauvegarder en local

  :param url: l'url à lire
  :param path: path du répertoire où sera stocké le fichier
  '''
  response = requests.get(url)
  local = get_local_form_response(response)
  response.raise_for_status()    # Check that the request was successful
  with open(path+local, "wb") as f:
    f.write(response.content)
  return(url,path+local)

# Lire une liste d'url
def read_all(lurl, path=""):
  '''
  :param url: liste des url à lire (un itérateur)
  :param path: path du répertoire où seront stocké les contenus récupérés
  '''
  
  for url in lurl:
    print(read_from_url(url, path))