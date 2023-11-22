def comprobar_divisa(divisas: dict, divisa: str) -> str:
    if divisa in divisas:
        return f"{divisa} = {divisas[divisa]}"
    else:
        return f"{divisa} no está en mi diccionario."


def main():

    info = {}

    nombre = input("Introduzca su nombre: ")
    edad = input("Introduzca su edad: ")
    direccion = input("Introduzca su dirección: ")
    teléfono = input("Introduzca su número de teléfono: ")

    print


if __name__ == "__main__":
    main()