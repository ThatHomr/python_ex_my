import oracletest

oracletest.create_table()

while True:
    display = '''
    ----------------------------------------------------------------------------------
    1. 명함 추가  2. 명함 수정  3. 명함 삭제  4. 명함 검색  5. 명함 리스트 출력  6. 종료
    ----------------------------------------------------------------------------------
    >>> '''
    menu = input(display)
    
    if menu == '1':
        try:
            oracletest.insert_card()
        except Exception as e:
            print(e)

    elif menu == '2':
        try:
            oracletest.update_card()
        except Exception as e:
            print(e)
    
    elif menu == '3':
        try:
            oracletest.delete_card()
        except Exception as e:
            print(e)

    elif menu == '4':
        try:
            oracletest.search_card()
        except Exception as e:
            print(e)

    elif menu == '5':
        try:
            oracletest.list_card()
        except Exception as e:
            print(e)
    
    elif menu == '6':
        print('프로그램 종료!')
        break

    else:
        print('메뉴선택을 잘못하셨습니다.')