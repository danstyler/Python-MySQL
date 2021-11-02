import pymysql.cursors
import admin


class admin():
    def __init__(self):
        pass

    def conexao(self):
        try:
            self.banco =  pymysql.connect(host='localhost',
                                        user='root',
                                        password='1234',
                                        db='projetoaeronaves',
                                        charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor)
            print('Conectado')
        except:
            print('erro ao conectar com a base de dados')

    def login(self):
        global autenticado
        self.conexao()
        email = input('Email: ')
        senha = input('Senha: ')
        autenticado = False
        try:
            with self.banco.cursor() as cursos:
                cursos.execute('SELECT * FROM admin')
                resultados = cursos.fetchall()
        except:
            print('erro ao fazer a consulta com o bd admin')
        for i in resultados:
            if email==i['email'] and senha==i['senha']:
                autenticado = True
                break
            else:
                autenticado = False
                pass
        
        if autenticado:
            self.menuAdmin()
        else:
            print("Dados errados! Tente novamente")
            self.login()
    
    def VerificaEmail(self, email):
        self.conexao()
        try:
            with self.banco.cursor() as cursos:
                cursos.execute("SELECT * FROM admin")
                resultados = cursos.fetchall()
        except:
            print('erro ao fazer a consulta com o bd admin')
        for i in resultados:
            if email==i['email']:
                return 1
            else:
                pass
        return 0

    def cadastro(self):
        cod = '123'
        codigo = input('Digite o código Verificador: ')
        if codigo==cod:
            nome = input('Nome: ')
            email = input('Email: ')
            senha = input('Senha: ')
            dados = [nome, email, senha, 1]
            self.conexao()
            n = self.VerificaEmail(email)
            if n==1:
                print('Email existe - Teste realizar o login')
                self.login()
            else:
                with self.banco.cursor() as cursos:
                    sql = "INSERT INTO admin (nome, email, senha, status) VALUES (%s, %s, %s,%s)"
                    cursos.execute(sql,dados)
                    self.banco.commit()
                    print("Cadastrado")
                    self.login()     
    def menuAdmin(self):
        print("\n1. Cadastrar nova aeronave\n2. Alterar dados aeronaves\n3. Deletar aeronave\n4. Listar Aeronaves\n0. Sair")
        op = int(input('Digite sua escolha: '))
        if op==0:
            return 0
        elif op==1:
            modelo = input("Modelo: ")
            ano = int(input("Ano: "))
            cor = input("Cor: ")
            tipo = int(input("Tipo (1. Avião | 2. Helicóptero | 3.Drone): "))
            dadosAeronaves = [modelo, ano, cor, tipo]
            aeronaves(dadosAeronaves).cadastrarAeronave(dadosAeronaves)
        elif op==2:
            aeronaves().alterarAeronave()
        elif op==3:
            aeronaves().deletarAeronave()
        elif op==4:
            aeronaves().listarAeronave()

class aeronaves(admin):
    def __init__(self):
        pass

    def cadastrarAeronave(self, dadosAeronaves):

        self.conexao()
        with self.banco.cursor() as cursos:
            sql = "INSERT INTO aeronaves (modelo, ano, cor, tipo) VALUES (%s, %s, %s, %s)"
            cursos.execute(sql, dadosAeronaves)
            self.banco.commit()
            print("Cadastrado")
            self.menuAdmin()
    
    def listarAeronave(self):
        self.conexao()
        try:
            with self.banco.cursor() as cursos:
                cursos.execute("SELECT * FROM aeronaves")
                aeronaves = cursos.fetchall()
        except:
            print('erro ao fazer a consulta com o bd aeronaves')
        print("\n----------------------\n------Lista de aeronaves------\n---------------------")
        for i in aeronaves:
            if i['tipo']==1:
                tipo = "Avião"
            elif i['tipo']==2:
                tipo = "Helicóptero"
            else:
                tipo = "Drone"
            print("idaeronave: {} - Modelo: {} - Ano: {} - Cor: {} - Tipo: {}".format(i['idaeronave'], i['modelo'], i['ano'], i['cor'], tipo))
        try:
            if autenticado:
                self.menuAdmin()
        except:
            main.main()

    def deletarAeronave(self):
        self.conexao()
        id = int(input('O id da aeronave que quer deletar: '))
        with self.banco.cursor() as cursos:
            cursos.execute("DELETE FROM aeronaves WHERE idAeronave={}".format(id))
            self.banco.commit()
            print("\nDeletado")
            self.menuAdmin()

    def alterarAeronave(self):
        self.conexao()
        id = int(input('O id da aeronave que quer alterar: '))
        try:
            with self.banco.cursor() as cursos:
                cursos.execute("SELECT * FROM aeronaves WHERE idaeronave={}".format(id))
                aeronave = cursos.fetchall()

        except:
            print('Erro ao fazer a consulta com o bd aeronaves')
        
        modelo = input("Modelo ({})".format(aeronave[0]['modelo']))
        ano = int(input("Ano ({})".format(aeronave[0]['ano'])))
        cor = input("Cor ({})".format(aeronave[0]['cor']))
        tipo = int(input("Tipo ({})".format(aeronave[0]['tipo'])))

        with self.banco.cursor() as cursos:
            cursos.execute("UPDATE aeronaves SET modelo='{}', ano={}, cor='{}', tipo={} WHERE idAeronave={}".format(modelo, ano, cor, tipo, id))
            self.banco.commit()
            print("\nAlterado")
            self.menuAdmin()
    
def main():
    print("1. Para logar como administrador\n2. Para cadastrar\n3. Ver catalogo\n.0 Para sair")
    op = int(input('Digite sua escolha: '))
    if op==1:
        admin().login()
    elif op==2:
        admin().cadastro()
    elif op==3:
        aeronaves().listarAeronave()
    else:
        pass


if __name__=='__main__':
    main()
