a = [1,2,3,4,5]

lista = [i**2 for i in a if i%2!=0]
print(lista)

n = 10
maior = 0
lista = [float(input("Digite um número")) for i in range(n)]
for i in lista:
    if i>maior:
        maior=i
print(lista)