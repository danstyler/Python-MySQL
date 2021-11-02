#Classe Pai
class aeronave():
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
#Comandos para a aeronave utilizar Flaps
    def utilizarFlaps(self):
        pass
#Comandos para movimentar Trem de pouso   
    def movimentarTP(self, comando):
        if comando==1:
            return("Baixando Trêm de Pouso")
        else:
            return("Recolhendo Trêm de Pouso")
#Comandos para acelerar
    def acelerar(self):
        pass

#nova classe herdeira
class helicoptero(aeronave):
    def __init__(self, modelo, ano, cor):
        super().__init__(modelo,ano,cor)

#Retorno Classe pai
cessna = aeronave("Cessna", 1960, "Branca")
print(cessna.cor)
print(cessna.movimentarTP(1))

#Retorno classe herdeira
heli = helicoptero("Sirkorsky R-4", 1940, "Cinza")
print(heli.modelo)
print(heli.movimentarTP(1))
