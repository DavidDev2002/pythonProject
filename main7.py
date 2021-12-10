def main():
    frase = input("Introduce una frase: ")
    spc = [x for x in frase if x not in 'aàäAÀÄeèéëEÈÉËiíïIÍÏoòóöOÒÓÖuúüUÚÜ']
    STRspc = "".join(spc)
    print(STRspc)
if __name__ == '__main__':
    main()
