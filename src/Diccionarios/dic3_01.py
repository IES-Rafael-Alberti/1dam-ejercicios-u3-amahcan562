def comprobar_divisa(divisas: dict, divisa: str) -> str:
    if divisa in divisas:
        return f"{divisa} = {divisas[divisa]}"
    else:
        return f"{divisa} no está en mi diccionario."


def main():

    divisas = {"Euro": "€", "Dollar": "$", "Yen": "¥"}

    divisa = input("Introduzca una divisa: ").title()

    print(comprobar_divisa(divisas, divisa))

if __name__ == "__main__":
    main()