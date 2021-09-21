"""

@author: Eduardo Alvear
"""

def punto1(carros):
    c_amarillo = 0
    c_rosa = 0
    c_roja = 0
    c_verde = 0
    c_azul = 0

    for auto in carros:
        if auto == 1 or auto == 2:
            c_amarillo += 1
        elif auto == 3 or auto == 4:
            c_rosa += 1
        elif auto == 5 or auto == 6:
            c_roja += 1
        elif auto == 7 or auto == 8:
            c_verde += 1
        elif auto == 9 or auto == 0:
            c_azul += 1

    return {
        "Autos amarillos": c_amarillo,
        "Autos rosa": c_rosa,
        "Autos rojos": c_roja,
        "Autos verdes": c_verde,
        "Autos azules": c_azul
    }


