def evaluar_numero(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

def main():
    while True:
        try:
            numero = int(input("Introduce un número (o escribe 'exit' para salir): "))
            evaluar_numero(numero)
        except ValueError:
            print("Por favor, introduce un número válido o 'exit' para salir.")
            continue

if __name__ == "__main__":
    main()
