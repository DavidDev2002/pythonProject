def main():
    username = list()
    department = list()
    classroom = list()

    regs = int(input("Cuantos valores quieres introducir: "))

    for i in range(regs):
        username.append(input("Introduce un nombre de usuario: "))
        department.append(input("Introduce un departamento: "))
        classroom.append(input("Introduce una clase: "))
    reg = {
        'username': username,
        'department': department,
        'classroom': classroom
    }

    #print(reg)

    for i in range(regs):
        #print(reg['username'][i])
        print(reg['username'][i] + '\t\t|' + reg['department'][i] + '\t\t|' + str(reg['classroom'][i]) + '\t\t|')
if __name__ == '__main__':
    main()