import numpy as np
import matplotlib.pyplot as plt
import pymysql
import pandas
import select
import os, sys, io, selectors
import socket

con = pymysql.connect(host='localhost',
        user='root',
        password='1234',
        db='cadastro',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
        
try:

    with con.cursor() as cur:

        cur.execute('SELECT * FROM pessoa')
        rows = cur.fetchall()
        for row in rows:
            (row['id'], row['name'],row['dtnascimento'])  
finally:
    
    con.close()



df = pandas.read_sql(rows,index_col=['id'])
rows[0:][0:]['name']


x = ['Daniel','ZYZZ','Ant']
y = [26,23,15]

plt.bar(x,y)
plt.xlabel("Pessoa")
plt.ylabel("Idade")
plt.title("My Plot")

plt.show()