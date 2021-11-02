
def miniMaxSum(arr):
    soma = 0
    maxnum = 0
    minnum = 0
    resultado = []
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if j==i:
                soma = soma
            else:
                soma = soma + arr[j]
        resultado.append(soma)
        soma = 0
    maxnum = max(resultado)
    minnum = min(resultado)
    print(minnum,maxnum)

miniMaxSum([1,3,5,7,9])