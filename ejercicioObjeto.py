"""

from random import randint

#sorteo para 5 personas
parti= ["pepito", "nemo","RoDi" "dino", "GRShits"]
print(parti[randint(0,4)])
"""

# sorteo para 5 personas, hay 3 premios
# ojo: una persona no puede ganar dos veces
from random import randint

pers= ["Pepe", "Sara", "Yoko", "So", "jose"]

veces = 0
while veces < 3:
    gano = (pers[randint(0,4)])
    print(gano)
    pers.remove(gano)
    veces = veces +1





# Soluciones del problema
from random import randint


parti= ["Pepe", "Sara", "Yoko", "So", "jose"]
cont = 1
while cont <= 3:
    ganador = parti[randint(0, len(parti -1)]
    print("El premio", cont, "es para", ganador)
    cont = cont + 1
    parti.remove(ganador)


