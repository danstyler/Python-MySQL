class aeronave():
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    
    def utilizarFlaps(self):
        pass
    
    def movimentarTP(self, comando):
        if comando==1:
            return("Baixando TP")
        else:
            return("Recolhendo TP")

    def acelerar(self):
        pass

cessna = aeronave("Cessna", 1960, "Branco")
print(cessna.cor)
print(cessna.movimentarTP(0))