def main():
    numx = int(input("Introdueix el número que comença l'interval: "))
    numo = int(input("Introdueix el número que acaba l'interval: "))
    while numx > numo:
        print("Error torna a introduir els teus valors:")
        numx = int(input("Introdueix el número que comença l'interval: "))
        numo = int(input("Introdueix el número que acaba l'interval: "))
    for x in range(numx, numo):
        print(x)

if __name__ == '__main__':
    main()