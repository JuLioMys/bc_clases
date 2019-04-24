
#En el archivo persona.py crear una clase Persona con atributo nombre
#despues instanciar un objeto de tipo persona
class Persona:
    nombre = None
    def __init__(self, un_nombre):
        self.nombre = un_nombre
        print("Me llamo",self.nombre)

humano = Persona("Pepito")