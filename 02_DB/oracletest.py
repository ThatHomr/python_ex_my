import oracledb

oracledb.init_oracle_client()

'''
drop table namecard;

drop sequence namecard_seq;

create sequence namecard_seq
increment by 1
start with 1
'''

# def create_table():
#     conn = oracledb.connect('SCOTT/TIGER@localhost:1521/xe')
#     cur = conn.cursor()
#     cur.execute(
#     '''
#     create table namecard(
#         cardid number primary key,
#         name varchar2(20),
#         address varchar2(20),
#         tel varchar2(20),
#         email varchar2(20)
#     )'''
#     )
#     conn.commit()
#     conn.close()

def create_table():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            sql = '''
            create table namecard(
                cardid number primary key,
                name varchar2(50),
                address varchar2(50),
                tel varchar2(50),
                email varchar2(50)
            )
            '''
            try:
                cur.execute(sql)
            except Exception as e:
                print(e)

def insert_card():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            name = input('이름을 입력하세요 >>> ')
            address = input('주소를 입력하세요 >>> ')
            tel = input('휴대폰번호를 입력하세요 >>> ')
            email = input('email을 입력하세요 >> ')
            sql = 'insert into namecard values(namecard_seq.NEXTVAL, :1, :2, :3, :4)'
            try:
                cur.execute(sql, (name, address, tel, email))
                conn.commit()
            except Exception as e:
                print(e)

# def update_card():
#     with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
#         with conn.cursor() as cur:
#             sql = 'update namecard set name = :1, address = :2, tel = :3, email = :4 where cardid = :5 '
#             cardid = input('cardid >>> ')
#             name = input('이름 >>> ')
#             address = input('주소 >>> ')
#             tel = input('전화번호 >>> ')
#             email = input('email >>> ')
#             try:
#                 cur.execute(sql, (name, address, tel, email, cardid))
#                 conn.commit()
#             except Exception as e:
#                 print(e)

def update_card():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            cardid_list = []
            for item in cur.execute('select * from namecard'):
                print(f'등록번호 : {item[0]}, 이름 : {item[1]}, 주소 : {item[2]}, 전화번호 : {item[3]}, 이메일 : {item[4]}')
                cardid_list.append(item[0])
            key = int(input('수정할 등록번호 >>> '))
            if key in cardid_list:
                col = input('수정할 항목(name, address, tel, email) >>> ')
                data = input('수정할 값 >>> ')
                sql = f'update namecard set {col} = :1 where cardid = :2'
                cur.execute(sql, (data, key))
                conn.commit()

def delete_card():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            cardid_list = []
            for item in cur.execute('select * from namecard'):
                print(f'등록번호 : {item[0]}, 이름 : {item[1]}, 주소 : {item[2]}, 전화번호 : {item[3]}, 이메일 : {item[4]}')
                cardid_list.append(item[0])
            key = int(input('삭제할 등록번호 >>> '))
            if key in cardid_list:
                sql = f'delete namecard where cardid = :1'
                cur.execute(sql, (key, ))
                conn.commit()

def search_card():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            cardid_list = []
            for item in cur.execute('select cardid from namecard'):
                cardid_list.append(item[0])
            print(cardid_list)
            key = int(input('검색할 등록번호 >>> '))
            if key in cardid_list:
                sql = f'select * from namecard where cardid = :1'
                cur.execute(sql, (key,))
                print(cur.fetchone())
            else:
                print('존재하지 않은 등록번호입니다.')

# def search_card():
#     with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
#         with conn.cursor() as cur:
#             sql = 'select * from namecard where name = :1'
#             name = input('검색할 이름을 입력하세요 >>> ')
#             try:
#                 cur.execute(sql, [name])
#                 print(cur.fetchone())
#             except Exception as e:
#                 print(e)

def list_card():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            key = input('정렬 키(name, tel, address, email) >>> ')
            sort = input('오름차순(asc), 내림차순(desc) >>> ')
            if key in ('name', 'tel', 'address', 'email'):
                sql = f'select * from namecard order by {key} {sort}'
                for item in cur.execute(sql):
                    print(f'등록번호 : {item[0]}, 이름 : {item[1]}, 주소 : {item[2]}, 전화번호 : {item[3]}, 이메일 : {item[4]}')

# def list_card():
#     with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
#         with conn.cursor() as cur:
#             sql = 'select * from namecard'
#             try:
#                 cur.execute(sql)
#                 for item in cur.fetchall():
#                     print(item)
#             except Exception as e:
#                 print(e)

if __name__ == '__main__':
    # create_table()
    # insert_card()
    # update_card()
    # delete_card()
    # search_card()
    # list_card()
    pass