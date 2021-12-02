# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    lst = list()
    num = int(input("Intoduce el numero de valores que tendra la lista: "))
    for x in range(num):
        lst.append(int(input("Introduce el valor a tu lista: ")))
    print(lst)
if __name__ == '__main__':
    main()
