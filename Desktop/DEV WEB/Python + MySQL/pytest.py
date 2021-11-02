import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="cadastro"
)

mycursor = mydb.cursor()

sql = "INSERT INTO pessoa (name, dtnascimento) VALUES (%s, %s)"
val = ("daniel", "1991-04-21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Dados inseridos com sucesso!!!")



mycursor.execute("CREATE TABLE pessoa (id int primary key auto_increment not null, name varchar(256) not null, dtnascimento date)")