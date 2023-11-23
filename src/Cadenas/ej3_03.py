def contar_letras_en_palabra(palabra: str, letra_a_contar: str) -> int:
    contador = 0
    for caracter in palabra:
        if caracter == letra_a_contar:
            contador = contador + 1
    return contador

def pedir_palabra_y_letra() -> tuple:
    palabra = input("Introduzca una palabra: ")
    letra = None
    while letra is None:
        try:
            letra = input("Indique la letra que quiere contar: ")
            if not letra.isalpha():
                raise NameError
        except NameError:
            print("ERROR! Has introducido un número.")
            letra = None
    return palabra, letra

def main():
    palabra, letra = pedir_palabra_y_letra()
    print(contar_letras_en_palabra(palabra, letra))

    #print(contar_letras_en_palabra(pedir_palabra_y_letra()))
    
if __name__ == "__main__":
    main() 