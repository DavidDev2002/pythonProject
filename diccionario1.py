def main():
    nombre = list()
    peso = list()
    diametro = list()
    distancia_a_la_tierra = list()
    x = int(input("Introduce el numero de planeras que quieres introducir: "))
    while x < 1:
        x = int(input("Introduce el numero de planeras que quieres introducir: "))

    for i in range(x):
        nombre.append(input("Introduce el nombre del planeta: "))
        peso.append(input("Introduce el peso del planeta: "))
        diametro.append(input("Introduce el diametro del planeta: "))
        distancia_a_la_tierra.append(input("Introduce la distancia a la tierra del planeta: "))

    planetas = {
        'nombre': nombre,
        'peso': peso,
        'diametro': diametro,
        'distancia': distancia_a_la_tierra
    }

    for y in range(x):
        print(planetas['nombre'][y] + '\t\t| ' + planetas['peso'][y] + '\t\t| ' + planetas['diametro'][y] + '\t\t| ' + planetas['distancia'][y] + '\t\t| ')
if __name__ == '__main__':
    main()