diccionario = {}
nombre_de_diccionario = {"nombre_clave":"valor"}
#ejemplo lista
personalist = ["Marce", 32, "Programador"]

#ejemplo diccionario
dic_persona= {"nombre":"Marce", "edad":32}

dic_persona= {"nombre":"Marce", "edad":32}
print(dic_persona)


dic_persona["edad"]= "mmm..cuanto me pones?"
print(dic_persona["edad"])
#crear un diccionario persona con claves nombre, edad, estatura, e imprimir
# cada uno de los valores de las claves en un print diferente

diccionario_persona = {"nombre":" Juana","edad":50, "estatura":170 }

print(diccionario_persona["nombre"])

print(diccionario_persona["edad"])

print(diccionario_persona["estatura"])


#Luego de cambiar la edad.. con un imput()... a otro valor e imprimir de nuevo.

diccionario_persona = {"nombre":" Juana","edad":50, "estatura":170 }

edad = 30
diccionario_persona["edad"]= 30 #cambiar de manera manual
print(diccionario_persona["edad"])


diccionario_persona["edad"]= input("Ingresa la edad:")# cambiar con el imput
print(diccionario_persona["edad"])


#Luego agregar un par clave "hobbie" que contenga una ***lista*** de hobbies e imprimir todo el diccionario.

diccionario_persona["Hobbies"]= ["futbol", "volley", "natacion"]

print()
