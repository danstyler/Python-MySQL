def staircase(n):
    cont_espaco = n-1
    str1 = ''
    str2 = ''
    while cont_espaco >=0:
        for i in range(cont_espaco,0,-1):
            str1 = str1 + ' '
        str2 = str2 + "#"
        str3 = str1 + str2
        print(str3)
        str1 = ''
        cont_espaco -= 1

staircase(10)
