from circulo import Circulo
from rectangulo import Rectangulo
from cadena import Cadena
from numero_romano import NumeroRomano
from numero_entero import NumeroEntero

def mostrar_menu():
    print("Selecciona una opción:")
    print("1. Calcular área y perímetro del círculo")
    print("2. Calcular área del rectángulo")
    print("3. Convertir cadena a mayúsculas")
    print("4. Convertir número entero a número romano")
    print("5. Convertir número romano a número entero")
    print("0. Salir")

def ejecutar_opcion(opcion):
    if opcion == '1':
        circulo = Circulo()
        print(f"Área del círculo: {circulo.area()}")
        print(f"Perímetro del círculo: {circulo.perimetro()}")
    elif opcion == '2':
        rectangulo = Rectangulo()
        print(f"Área del rectángulo: {rectangulo.area()}")
    elif opcion == '3':
        cadena = Cadena()
        cadena.get_string()
        cadena.print_string()
    elif opcion == '4':
        numero_romano = NumeroRomano()
        numero_romano.get_numero()
        print(f"El número en romano es: {numero_romano.convertir_a_romano()}")
    elif opcion == '5':
        numero_entero = NumeroEntero()
        numero_entero.get_numero_romano()
        print(f"El número entero es: {numero_entero.convertir_a_entero()}")
    elif opcion == '0':
        print("Saliendo del programa...")
    else:
        print("Opción no válida")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        if opcion == '0':
            break
        ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()