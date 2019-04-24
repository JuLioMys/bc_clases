
class Dino: # Class es la receta para crear un objeto
    patas= 4   # Patas y nombre son parametros
    nombre = None
    def __init__(self, un_nombre): # "self" se refiere al objeto
        self.nombre =un_nombre
        print("Soy un dinosaurio",",me llamo", self.nombre")

    def get_patas(self):
        return self.patas
    
    def set_patas(self, cantidad):
        self.patas= cantidad

        def cortar_patas (self):
            self.patas= self.patas -1

pepito = Dino(4, "Pepito")


"""
#En el archivo persona.py crear una clase Persona con atributo nombre
#despues instanciar un objeto de tipo persona
class Persona:
    nombre = None
    def __init__(self, un_nombre):
        self.nombre = un_nombre

humano = Persona("Pepito")
"""
#Modificar la clase persona, agregarle atributo edad y 
# un metodo get_edad
#inicializar/crear un objeto de tipo persona y hacerle complor
#anhos

class Persona:
    nombre= None
    edad= None
    def __init__(self, el_nombre,la_edad):
        self.nombre= el_nombre
        self.edad= la_edad
        print("Hola! Mi nombre es", self ,nombre,"y tengo", edad, "anhos" )
    
    def get_nombre(self, nombre):
        return self.nombre

    def get_edad(self):
        self.edad = self.edad +1
        


