def main():

    print("—> Cálculadora básica <—")

    print("\nSelecciona una operación:\n0: Salir\n1: Suma\n2: Resta\n3: Multiplicación\n4: División\n")

    while True:

        user_option = int(input("Opción: "))

        if user_option == 0:

            print(f"\n¡Hasta pronto!")

            break

        elif user_option == 1:

            a = int(input("\nPrimer sumando: "))
            b = int(input("Segundo sumando: "))

            sum = a + b

            print(f"\nEl resultado de la suma es: {sum}\n")

        elif user_option == 2:

            a = int(input("\nMinuendo: "))
            b = int(input("Sustraendo: "))

            sub = a - b

            print(f"\nEl resultado de la resta es: {sub}\n")

        elif user_option == 3:

            a = int(input("\nMultiplicando: "))
            b = int(input("Multiplicador: "))

            multi = a * b

            print(f"\nEl resultado de la multiplicación es: {multi}\n")

        elif user_option == 4:

            a = int(input("\nDividendo: "))
            b = int(input("Divisor: "))

            div = a / b

            print(f"\nEl resultado de la división es: {div}\n")

        else:

            print("\nInserta un número válido.\n")

if __name__ == "__main__":
    main()