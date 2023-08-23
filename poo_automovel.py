class Automovel:

    def __init__(self, placa):
        print("Executando o construtor...")
        self.set_placa(placa) 
    def get_placa(self,):
        return self.__placa
    def set_placa(self, placa):
        if len(placa) < 5:
            print("A placa nao pode ser registrado por nao ter digitos suficientes")
            self.__placa = None
        else:
            self.__placa = placa
    def dirigir(self, velocidade):
        print("Estou dirigindo a %d km/h" %velocidade)                

corola = Automovel('RJ123')
fusca = Automovel("123")
fit = Automovel('256323')
peugeot = Automovel('NI26')

print(corola.get_placa())
print(fusca.get_placa())
print(fit.get_placa())
print(peugeot.get_placa())
