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
        return("Forma na qual aeronave acelera")

#nova classe herdeira
class helicoptero(aeronave):
    def __init__(self, modelo, ano, cor):
        super().__init__(modelo,ano,cor)
    
    def acelerar(self):
        return("Forma no qual helicoptero acelera")

heli = helicoptero("Sirkorsky R-4", 1940, "Cinza")
aviao = aeronave("Cessna", 1960, "branco")

aeronaves = [heli, aviao]

for i in aeronaves:
    print(i.acelerar())