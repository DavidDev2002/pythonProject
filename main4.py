def main():

    apr = 0
    napr = 0
    sus = 0
    nsus = 0
    i = 0
    x = int(input("Indica cuantas notas vas a introducir: "))

    for y in range(x):
        notas = (int(input("Introduce las notas: ")))
        while notas < 0 or notas > 10:
            notas = (int(input("Introduce las notas: ")))
        if notas >= 5:
            apr += 1
            napr += notas
        else:
            sus += 1
            nsus += notas

    mita = napr / apr
    mits = nsus / sus

    print("Nota media de aprobados: ", mita)
    print("Total de aprobados: ", apr)
    print("Nota media de suspensos: ", mits)
    print("Total de suspensos: ", sus)

if __name__ == '__main__':
    main()

