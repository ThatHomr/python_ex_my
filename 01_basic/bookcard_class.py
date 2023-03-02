import bookcard as nc
import pickle

booklist = None

with open('01_basic/booklist.pickle', 'rb') as f:
    booklist = pickle.load(f)

# 1.저장,2.수정,3.삭제,4.리스트,5.검색,6.종료(Q)

while True:
    menu = input('''
    -----------------------------------------------------------------------------
    1.저장 2.수정 3.Book 삭제 4.Book 내용 보기 5.전체목록 보기 6.종료 
    ''')

    if menu == '1':
        if booklist == None:
            booklist = nc.BookList(input('booklist 제목을 입력하세요 >>> '))
        
        else:
            num = input('일련번호 >>> ')
            name = input('책 제목 >>> ')
            company = input('출판사 >>> ')
            book = nc.Book(num, name, company)
            booklist.add_Book(book)
    
    elif menu == '2':
        if booklist == None:
            print('booklist가 없습니다.')
        else:
            num = input('수정할 일련번호 >>> ')
            name = input('수정할 책 제목 >>> ')
            company = input('수정할 출판사 >>> ')
            book = nc.Book.write_card(num, name, company)
            booklist.add_Book(book)
    
    elif menu == '3':
        if booklist == None:
            print('BookList를 생성한 후 가능합니다.')
        else:
            print(list(booklist.books.keys()))
            page = int(input('book number >>> '))
            book = booklist.remove_book(page)
            print(book, '-> 삭제')

    elif menu == '4':
        if booklist == None:
            print('BookList를 생성한 후 가능합니다.')
        else:
            print(list(booklist.books.keys()))
            page = int(input('book number >>> '))
            book = booklist.books[page]
            print(book)

    elif menu == '5':
        if booklist == None:
            print('BookList를 생성한 후 가능합니다.')
        else:
            key = input('정렬 키(입력값:num, name, company) >>>')
            sort = bool(input('오름차순(enter), 내림차순(1) >>> '))
            
            if key in ('num', 'name', 'company'):
                booklist.list_books(key, sort)
            else:
                booklist.list_books(reverse=sort)
    
    elif menu == '6':
        print('프로그램 종료')
        break

with open('01_basic/booklist.pickle', 'wb') as f:
    pickle.dump(booklist, f)

