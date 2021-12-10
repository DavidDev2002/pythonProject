def main():
    frase = "Practica els problemes de list comprehensions per a ser més Pythonic!"
    spc = [i for i in frase.split() if len(i) < 5]
    print(spc)
if __name__ == '__main__':
    main()