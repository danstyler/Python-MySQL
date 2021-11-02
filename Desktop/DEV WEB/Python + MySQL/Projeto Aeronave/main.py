import admin as adm

def main():
    print("1. Para logar como administrador\n2. Para cadastrar\n3. Ver catalogo\n.0 Para sair")
    op = int(input('Digite sua escolha: '))
    if op==1:
        adm.admin().login()
    elif op==2:
        pass
    elif op==3:
        pass
    else:
        pass


if __name__=='__main__':
    main()

