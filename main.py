# Main Taller collaboration de python
from fibonacci import calcular_fibonacci
from factorial import calcular_factorial
from primos import es_primo
from perfectos import generar_numeros_perfectos

def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Cálculo de Fibonacci")
    print("2. Cálculo del factorial de un número")
    print("3. Determinar si un número es primo")
    print("4. Generar los primeros N números perfectos")
    print("5. Calcular el MCD de dos números")
    print("6. Invertir un texto ")
    print("7. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            n = int(input("Ingrese un número entero positivo: "))
            print(f"Fibonacci de {n} es: {calcular_fibonacci(n)}")

        elif opcion == "2":
            n = int(input("Ingrese un número entero positivo: "))
            print(f"El factorial de {n} es: {calcular_factorial(n)}")

        elif opcion == "3":
            n = int(input("Ingrese un número entero positivo: "))
            if es_primo(n):
                print(f"El número {n} SÍ es primo.")
            else:
                print(f"El número {n} NO es primo.")

        elif opcion == "4":
            n = int(input("Ingrese cuántos números perfectos desea generar: "))
            print(f"Los primeros {n} números perfectos son: {generar_numeros_perfectos(n)}")

        elif opcion == "5":
            from mcd import calcular_mcd
            a = int(input("Ingrese el primer número entero positivo: "))
            b = int(input("Ingrese el segundo número entero positivo: "))
            print(f"El MCD de {a} y {b} es: {calcular_mcd(a, b)}")

        elif opcion == "6":
            from invertir_texto import invertir_texto
            texto = input("Ingrese el texto que desea invertir: ")
            print(f"Texto invertido: {invertir_texto(texto)}")

        elif opcion == "7":
            print("¡Gracias por usar el programa!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()