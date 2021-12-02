"""
1. Demana a l'usuari quants registres vol introduir(validar nat)
2. Por cada registro pedir:
    - nombre apellido1 apellido2 y mostrar su codigo de nombre
    - telefono
    - edad
    - contacto(bool)
3. Retorna per cada registre per pantalla en format taula."""


def main():
    #Ejercicio 2
    lst = list()
    num = int(input("Intoduce el numero de valores que tendra la lista: "))
    while num < 1:
        num = int(input("Intoduce el numero de valores que tendra la lista: "))
    for x in range(num):
        name = (input("Introduce el nombre: "))
        firstname = (input("Introduce el apellido: "))
        lastname = (input("Introduce el 2º apellido: "))
        codigo = firstname[:2] + lastname[:2] + name[:2]
        lst.append(codigo)
        lst.append(int(input("Introduce el telefono: ")))
        lst.append(int(input("Introduce la edad : ")))
        lst.append(bool(input("Introduce si te han contactado o no: ")))
    print(lst)
if __name__ == '__main__':
    main()