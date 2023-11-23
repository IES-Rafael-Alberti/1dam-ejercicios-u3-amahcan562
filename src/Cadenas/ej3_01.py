def main():
    cadena = "Mi nombre es Andrés."
    longitud = len(cadena)

    while longitud > 0:
        longitud -= 1
        print(cadena[longitud])
        

if __name__ == "__main__":
    main() 