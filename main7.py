def main():
    frase = input("Introduce una frase: ")
    spc = [x for x in frase if x not in 'aáàäeéèëiíìïoóòöuúùü']
    print(spc)
if __name__ == '__main__':
    main()
