import pymysql
import select
import os, sys, io, selectors
import socket
import matplotlib.pyplot as plt

con = pymysql.connect(host='localhost',
        user='root',
        password='1234',
        db='cadastro',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
        
try:

    with con.cursor() as cur:

        cur.execute("SELECT id, name, (YEAR(now())-YEAR(dtnascimento)) as 'idade' FROM pessoa")
        rows = cur.fetchall()
        for row in rows:  
            print(row['id'], row['name'],row['idade'])
finally:
    
    con.close()

x=[]
y=[]

for i in rows:
    x.append(i['name'])
    y.append(i['idade'])

plt.bar(x,y)
plt.xlabel("Pessoa")
plt.ylabel("idade")
plt.title("My Plot")
plt.show()