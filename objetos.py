
class Dino: # Class es la receta para crear un objeto
    patas= 4   # Patas y nombre son parametros
    nombre = None
    def __init__(self, canti_patas, un_nombre): # "self" se refiere al objeto
        self .patas= canti_patas
        self.nombre =un_nombre
        print("Soy un dinosaurio",",me llamo", self, nombre, "y tengo", patas,)
    def get_patas(self):
        return self.patas
    def set_patas(self, cantidad)
pepito = Dino(4, "Pepito")


"""
#En el archivo persona.py crear una clase Persona con atributo nombre
#despues instanciar un objeto de tipo persona
class Persona:
    nombre = None
    def __init__(self, un_nombre):
        self.nombre = un_nombre

humano = Persona("Pepito")

