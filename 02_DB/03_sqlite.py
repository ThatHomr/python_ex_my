import sqlite3
import os

path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '/example.db')
cur = conn.cursor()
# select *from stocks where symbol = 'rhat'
symbol = input('종목이름을 입력하세요 >>> ')

# sql = "select *from stocks where symbol = '%s'" % symbol
sql = "select * from stocks where symbol = ?"
cur.execute(sql, (symbol,))
print(cur.fetchone())

conn.close()