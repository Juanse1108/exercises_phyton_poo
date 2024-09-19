# Escribir una clase en python que convierta un número romano en un
# número entero
class NumeroEntero:
    def __init__(self):
        self.romano = ""
    
    def get_numero_romano(self):
        self.romano = input("Ingrese un número romano: ").upper()
    
    def convertir_a_entero(self):
        valores = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }

        total = 0
        prev = 0

        for letra in reversed(self.romano):
            valor = valores.get(letra, 0)
            if valor >= prev:
                total += valor
            else:
                total -= valor
            prev = valor
        
        return total
