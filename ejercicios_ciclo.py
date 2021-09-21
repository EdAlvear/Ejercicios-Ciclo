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

def punto3(horas_obrero):
    for obrero in horas_obrero:
        if obrero <= 40:
            print(f'Pago: {obrero * 20}')
        elif obrero > 40:
            print(f'Pago: {40 * 20 + ((obrero - 40) * 25)} ')

def punto4(edad_hombres, edad_mujeres):
    acumulador_hombres = acumulador_mujeres = total = 0
    for edad in edad_hombres:
        acumulador_hombres += edad
        total += edad
    for edad in edad_mujeres:
        acumulador_mujeres += edad
        total += edad
    
    return {
        "Promedio hombres": acumulador_hombres / len(edad_hombres),
        "Promedio mujeres": acumulador_mujeres / len(edad_mujeres),
        "Promedio general": total / (len(edad_hombres) + len(edad_mujeres))
    }

def punto5(numbers):
    menor = numbers[len(numbers) - 1]
    for n in numbers:
        if n < menor:
            menor = n
    return menor

def punto6():
    for i in range(5):
        ultimo_peso = int(input('Ingrese su ultimo peso:'))
        prom_pesos = 0
        for i in range(10):
            prom_pesos += int(input(f'Ingrese el peso de la bascula {i}:'))

        prom_pesos = prom_pesos / 10

        if prom_pesos > ultimo_peso:
            print(f'SUBIÓ {prom_pesos - ultimo_peso}')
        else:
            print(f'BAJÓ {ultimo_peso - prom_pesos}')


def punto7(num_productos):

    total = 0
    for _ in range(num_productos):
        precio = int(input('Ingrese el precio del producto: '))
        cantidad = int(input('Cantidad del producto: '))

        total += precio * cantidad
    return total


def punto8(num_entradas, valor):
    edad1 = edad2 = edad3 = edad4 = edad5 = 0
    for i in range(num_entradas):

        edad = int(input('Ingrese su edad: '))
        if edad < 5:
            print('No puede ingresar')
        if edad >= 5 and edad <= 14:
            edad1 += valor * 0.35
        if edad >= 15 and edad <= 19:
            edad2 += valor * 0.25
        if edad >= 20 and edad <= 45:
            edad3 += valor * 0.1 
        if edad >= 46 and edad <= 65:
            edad4 += valor * 0.25
        if edad > 65:
            edad5 += valor * 0.35

    return {
        "Categoria 1": edad1,
        "Categoria 2": edad2,
        "Categoria 3": edad3,
        "Categoria 4": edad4,
        "Categoria 5": edad5,
        }