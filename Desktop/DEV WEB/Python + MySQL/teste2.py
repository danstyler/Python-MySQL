nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1+nota2+nota3)/3


def mediaNota(media):
    if media >=6:
        print("Aprovado com media: {}".format(round(media,2)))
    elif media > 4 and media < 6:
        print("Recuperação com media: {}".format(round(media,2)))
    elif media < 4:
        print("Reprovado com media: {}".format(round(media,2)))

mediaNota(media)

