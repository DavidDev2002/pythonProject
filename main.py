def main():
    #Ejercicio de Codigo de nombre
    nombre = input("Introduce tu nombre: ")
    apellido = input("Introduce tu apellido: ")
    segundo = input("Introduce tu 2º apellido: ")

    print("Este es tu codigo: ",apellido[:2] + segundo[:2] + nombre[:2])
if __name__ == '__main__':
    main()
