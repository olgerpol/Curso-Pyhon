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
    

if __name__ == "__main__":
    numeroaevaluar = Numero(int(input("Ingrese un numero: \n")))
    numeroaevaluar.evaluarNumero()
    sumarealizada = numeroaevaluar.sumar(2)
    print("\nLa suma realizada es: ", sumarealizada)
