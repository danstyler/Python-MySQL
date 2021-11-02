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
try:

    with con.cursor() as cur:

        cur.execute('DELETE FROM pessoa WHERE name = %s',(pessoa))
        con.commit()
        print(str(con.commit()),' Registros Excluídos')
finally:
    
    con.close()