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


def punto2(animal):
    edad_animales = []
    if animal.lower() == 'elefante':
        for i in range(20):
            elefante = int(input('Digite la edad del elefante:'))
            edad_animales.append(elefante)
    if animal.lower() == 'jirafa':
        for i in range(15):
            jirafa = int(input('Digite edad de la jirafa:'))
            edad_animales.append(jirafa)
    if animal.lower() == 'chimpance':
        for i in range(40):
            chimpance = int(input('Digite la edad del chimpance:'))
            edad_animales.append(chimpance)
    
    c1 = c2 = c3 = 0
    for edad in edad_animales:
        if edad >= 0 and edad <= 1:
            c1 += 1
        elif edad > 1 and edad < 3:
            c2 += 1
        elif edad >= 3:
            c3 += 1
    
    if animal.lower() == 'elefante':
        c1 = (c1 * 100) / 20 
        c2 = (c2 * 100) / 20
        c3 = (c3 * 100) / 20
        
    if animal.lower() == 'jirafa':
        c1 = (c1 * 100) / 15 
        c2 = (c2 * 100) / 15
        c3 = (c3 * 100) / 15
        
    if animal.lower() == 'chimpance':
        c1 = (c1 * 100) / 40
        c2 = (c2 * 100) / 40
        c3 = (c3 * 100) / 40


    return {
        "animal": animal,
        "Entre 0 y 1 año": c1,
        "Entre 1 y 3 años": c2,
        "Mayor o igual a 3 años": c3
    }
