def main():
    frase = "Practica els problemes de list comprehensions per a ser més Pythonic!"
    spc = [x for x in frase if x in ' ']
    print(len(spc))
if __name__ == '__main__':
    main()
