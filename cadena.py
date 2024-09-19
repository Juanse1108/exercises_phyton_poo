# Escribir una clase en python con 2 métodos: get_string y print_string.
# get_string acepta una cadena ingresada por el usuario y print_string
# imprime la cadena en mayúsculas.
class Cadena:
    def __init__(self):
        self.cadena = ""
    
    def get_string(self):
        self.cadena = input("Ingrese una cadena: ")
    
    def print_string(self):
        print(self.cadena.upper())