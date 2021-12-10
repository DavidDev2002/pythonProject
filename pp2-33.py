def main():
    #Donat el següent array:
    #char[] arrayNotes = {'a', 'z', 'g', 'd', 'w', 'o', 'h', 'e', 'x', 's'};
    #Dissenya un programa on l’usuari ha d’introduir una lletra i l’algoritme ha de validar si    aquesta es troba a l’array.
    letras = ['a', 'z', 'g', 'd', 'w', 'o', 'h', 'e', 'x', 's']
    check = input("Introduce una letra: ")
    if check in letras:
        print("La lletra introduiza esta la lista.")
    else:
        print("La letra no esta en la lista.")
if __name__ == '__main__':
    main()