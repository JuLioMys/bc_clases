import requests

from pprint import pprint
"""
API_KEY= "595695c3"
URL = "http://www.omdbapi.com/?apikey="

titulo= "The Matrix"
busqueda = URL + API_KEY + "&t=" + titulo
print(busqueda)
respuesta = requests.get(busqueda)

dic_peli = respuesta.json()

pprint(dic_peli)
print(dic_peli["Year"])
"""

#Ejercio 1
#Consultar el API de omdb e imprimir el nombre del director de 
# Fight Club

API_KEY= "595695c3"
URL = "http://www.omdbapi.com/?apikey="

titulo= "Fight Club"
busqueda = URL + API_KEY + "&t=" + titulo
print(busqueda)
respuesta = requests.get(busqueda)

dic_peli = respuesta.json()

pprint(dic_peli)
print(dic_peli["Director"])



#Ejercicio 2
# Crear una funcion que reciba como argumento el titulo de una peli
# y retorne los actores de esa peli


def funcion(arg_titulo):
    API_KEY= "595695c3"
    URL = "http://www.omdbapi.com/?apikey="
    busqueda = URL + API_KEY + "&t=" + arg_titulo
    print(busqueda)
    respuesta = requests.get(busqueda)

    dic_peli = respuesta.json()

    pprint(dic_peli)
    print(dic_peli["Actors"])

funcion("Fight Club")


