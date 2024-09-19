# Escribir una clase en python llamada rectángulo que contenga una base
# y una altura, y que contenga un método que devuelva el área del
# rectángulo.
class Rectangulo:
    def __init__(self):
        self.base = float(input("Ingrese la base del rectángulo: "))
        self.altura = float(input("Ingrese la altura del rectángulo: "))
    
    def area(self):
        return self.base * self.altura