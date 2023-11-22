def main():
    total = 0
    asignaturas = {"Matemáticas": 6, 'Física': 4, 'Química': 5}
    for asignatura,credits in asignaturas.items():
        print(f"{asignatura} tiene {credits}.")
        total += credits
    print(f"Total = {total}.")


if __name__ == "__main__":
    main()