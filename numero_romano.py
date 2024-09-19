# Escribir una clase en python que convierta un número entero a número
# romano
class NumeroRomano:
    def __init__(self):
        self.num = 0
    
    def get_numero(self):
        self.num = int(input("Ingrese un número entero: "))
    
    def convertir_a_romano(self):
        if not (1 <= self.num <= 3999):
            return "El número debe estar entre 1 y 3999"

        valores = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        resultado = ""
        num = self.num
        
        for valor, simbolo in valores:
            while num >= valor:
                resultado += simbolo
                num -= valor

        return resultado
