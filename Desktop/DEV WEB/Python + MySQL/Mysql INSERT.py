import pymysql
import select
import os, sys, io, selectors
import socket

con = pymysql.connect(host='localhost',
        user='root',
        password='1234',
        db='cadastro',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)

pessoa=('robertviado','2005-04-05')

try:

    with con.cursor() as cur:

        cur.execute('INSERT INTO pessoa (name,dtnascimento) VALUES (%s,%s)', (pessoa[0],pessoa[1]))
        con.commit()
        print('nova pessoa inserida')
finally:
    
    con.close()