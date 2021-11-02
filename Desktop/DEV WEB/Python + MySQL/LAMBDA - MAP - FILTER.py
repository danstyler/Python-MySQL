def quadrado(n): return n**2
lambda n: n**2

a = [1,2,4,5,3,5,6]

def quadrado(n):
    for i in range(0,len(n)):
        n[i] = n[i]**2
    return n
quadrado(a)

a = [1,2,4,5,3,5,6]
def quadrado(n): return n**2
list(map(quadrado, a))

a = [1,2,4,5,3,5,6]
list(map(lambda n: n**2, a))


a = [1,2,4,5]
list(filter(lambda i: i%2==0, a))