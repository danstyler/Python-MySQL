a = {"Marca": "Ford", "modelo": "Mustang", "ano": 2020}

x = a.get("modelo")


print(x)

a["ano"] = 2019
print(a)


a = {"carro1": {"Marca": "Ford", "modelo": "Mustang", "ano": 2020}, "carro2": {"Marca": "Fiat", "modelo": "Uno", "ano": 2018}}


print(a["carro2"]["Marca"])

a = (1,23,3,1)
b = [1,23,3,1]

print(max(a), max(b))
print(min(a), min(b))
print(len(a), len(b))
print(a.count(3))

tupla = ([2,1], [3,3])
tupla[0][0] = 9
print(tupla)


def quadrado(a):
    return a*a
quadrado(5)

def duplica(s1, s2):
    s2 = s1
    print(s1, s2)

duplica("Meu cachorro", "Amarelo e preto")

def main():
    a = int(input("Digite um numero: "))
    quadrado(a)


nota1 = float(input("Digite a primeira nota: "))
peso1 = float(input("Digite o peso da primera nota: "))
nota2 = float(input("Digite a segunda nota: "))
peso2 = float(input("Digite o peso da segunda nota: "))

mediap = (nota1+nota2)/(peso1+peso2)


txt = "Daniel lucas dos santos"

lista= "Daniel lucas dos santos".split()

print(lista)
print('A média ponderada é {}'.format(mediap))
("Daniel lucas dos santos").split


dados = (["daniel","santos","lucas"],["2020-04-01","2020-04-02","2020-04-03"], [222,333,444])

dados[0][1]= "Zyzz"

print(dados)

dados = ({"id1":"pluma","id2":"bingo","id3":"branca"},{"id1":"2001-04-01","id2":"2002-09-20","id3":"2003-10-30"},{"id1":"111","id2":"222","id3":"333"})


email = "dan_santtos@live.com"


def retornaDominio(email):
    email = input("Informe seu email: ")
    print(email.split("@")[1])