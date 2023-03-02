import book

book.create_table()

while True:
    prompt = '''
    --------------------------------------------------------------------------------
    1. 책정보 등록  2. 책정보 수정  3. 책정보 삭제  4. 책 리스트 출력  5. 검색  6. 종료
    --------------------------------------------------------------------------------
    >>> '''
    menu= input(prompt)
    if menu == '1':
        try:
            book.insert_books()
        except Exception as e:
            print(e)

    elif menu == '2':
        try:
            book.update_book()
        except Exception as e:
            print(e)

    elif menu == '3':
        try:
            book.delete_book()
        except Exception as e:
            print(e)

    elif menu == '4':
        num = int(input('전체 출력(0), 개수출력(숫자) >>> '))
        try:
            if num == '':
                book.all_books()
            else:
                book.some_books(num)
        except Exception as e:
            print(e)

    elif menu == '5':
        title = input('검색 할 책 제목 >>> ')
        try:
            book.one_book(title)
        except Exception as e:
            print(e)

    elif menu == '6':
        print('프로그램 종료!')
        break

    else:
        print('메뉴선택을 잘못하셨습니다.')
