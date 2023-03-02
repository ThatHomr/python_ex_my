import cx_Oracle

try:
    conn = cx_Oracle.connect('SCOTT/TIGER@localhost:1521/xe')
    cur = conn.cursor()
    sql = 'update dept set DNAME = :1, LOC = :2, where DEPTNO = :3 '
    print(cur.fetchall())
    deptno = input('부서코드 >>> ')
    dname = input('수정할 부서이름 >>> ')
    loc = input('수정할 지역이름 >>> ')
    data = {dname, loc, deptno}
    cur.execute(sql, data)
    conn.commit()
    conn.close()
except Exception as e:
    print(e)
    print()

