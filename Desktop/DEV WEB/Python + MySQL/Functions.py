a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

def verificaT(a,b,c):
    if a==b and b==c:
        print("Triangulo equilatero")
elif a==b or b==c or c==a:
        print("Triangulo Isosceles")
    else:
        print("Triangulo Escaleno")

verificaT(a,b,c)


