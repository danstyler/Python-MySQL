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

pessoa='lucas'
newpessoa='l'
try:

    with con.cursor() as cur:

        cur.execute('UPDATE pessoa SET name = %s WHERE name = %s',(pessoa,newpessoa))
        con.commit()
        print('Dados alterados')
finally:
    
    con.close()