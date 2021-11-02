import pymysql

con = pymysql.connect('localhost', 'root',
    '1234', 'cadastro')

try:

    with con.cursor() as cur:

        cur.execute('SELECT VERSION()')

        version = cur.fetchone()

        print(f'Database version: {version[0]}')

finally:

    con.close()