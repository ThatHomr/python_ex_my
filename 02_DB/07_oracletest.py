import cx_Oracle

conn = cx_Oracle.connect('SCOTT/TIGER@localhost:1521/xe')

cur = conn.cursor()

sql = "select * from emp"

cur.execute(sql)
for item in cur.fetchali():
    print(item)

conn.close()