#Classe Pai
class aeronave():
    def __init__(self, modelo, ano, cor, matricula):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.__matricula = matricula
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
    def __init__(self, modelo, ano, cor, matricula):
        super().__init__(modelo,ano,cor,matricula)
    
    def acelerar(self):
        return("Forma no qual helicoptero acelera")

heli = helicoptero("Sirkorsky R-4", 1940, "Cinza", 12)
aviao = aeronave("Cessna", 1960, "branco", 11)

print(aviao._aeronave__matricula)
print(heli._aeronave__matricula)