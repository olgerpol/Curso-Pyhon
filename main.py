from dataclasses import dataclass

@dataclass  
class Numero:
    numero: int
    
    def evaluarNumero(self):
        if self.numero & 1:  # Verifica si es impar
            print("impar")
            if self.numero == 7:
                print("\nEl numero ingresado es un comodin")
        else:  # Si no es impar, entonces es par
            print("par")
            if self.numero == 10:
                print("\nEl numero ingresado es 10")
    
    def sumar(self, numeroasumar):
        return self.numero + numeroasumar
    
    def es_primo(self):
        if self.numero <= 1:
            return False
        for i in range(2, int(self.numero**0.5) + 1):
            if self.numero % i == 0:
                return False
        return True
    
    def factorial(self):
        if self.numero < 0:
            return "No se puede calcular el factorial de un número negativo."
        resultado = 1
        for i in range(1, self.numero + 1):
            resultado *= i
        return resultado
    
    def tabla_multiplicar(self):
        print(f"\nTabla de multiplicar del {self.numero}:")
        for i in range(1, 11):
            print(f"{self.numero} x {i} = {self.numero * i}")
    
    def es_numero_perfecto(self):
        suma_divisores = sum(i for i in range(1, self.numero) if self.numero % i == 0)
        return suma_divisores == self.numero

if __name__ == "__main__":
    numeroaevaluar = Numero(int(input("Ingrese un numero: \n")))
    numeroaevaluar.evaluarNumero()
    sumarealizada = numeroaevaluar.sumar(2)
    print("\nLa suma realizada es: ", sumarealizada)
    
    # Verificar si es primo
    if numeroaevaluar.es_primo():
        print(f"\nEl número {numeroaevaluar.numero} es primo.")
    else:
        print(f"\nEl número {numeroaevaluar.numero} no es primo.")
    
    # Calcular el factorial
    print(f"\nEl factorial de {numeroaevaluar.numero} es: {numeroaevaluar.factorial()}")
    
    # Mostrar la tabla de multiplicar
    numeroaevaluar.tabla_multiplicar()
    
    # Verificar si es un número perfecto
    if numeroaevaluar.es_numero_perfecto():
        print(f"\nEl número {numeroaevaluar.numero} es un número perfecto.")
    else:
        print(f"\nEl número {numeroaevaluar.numero} no es un número perfecto.")

