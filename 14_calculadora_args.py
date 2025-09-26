class Calculadora:
    def somar(self, *args):
        return sum(args)
    
    def media(self, *args):
        resultado = sum(args) / len(args)
        return resultado
    
calc = Calculadora()
print(calc.somar(2,4,10))
print(calc.media(2,4,10))

