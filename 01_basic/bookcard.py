# 도서관리 프로그램
# 데이터 구조는 리스트를 이용
# 일련번호,책이름,출판사,....
# 1.저장,2.수정,3.삭제,4.리스트,5.검색,6.종료(Q)

class Book:
    def __init__(self, num, name, company) -> None:
        self.num = num
        self.name = name
        self.company = company

    def write_card(self, num, name, company):
        self.num = num
        self.name = name
        self.company = company

    def remove_all(self):
        self.num = ''
        self.name = ''
        self.company = ''

    def __str__(self):
        return f'num:{self.num}, name:{self.name}, company:{self.company}'

class BookList:
    def __init__(self, title):
        self.title = title
        self.book_number = 1
        self.books = {}
    
    def add_Book(self, book, page=0):
        if self.book_number < 300:
            if page == 0:
                self.books[self.book_number] = book
                self.book_number += 1
            else:
                self.books = {page:book}
                self.book_number += 1
        else:
            print('책이 있습니다.')
    
    def remove_book(self, book_number):
        if book_number in self.books.keys():
            return self.books.pop(book_number)
        else:
            print('해당 책은 존재하지 않습니다.')

    def list_books(self, key=None, reverse=False):

        if key == None:
            for page in self.books:
                print(self.books[page])

        else:
            sorted_dict = sorted(self.books.items(), key= eval(f'lambda item: item[1].{key}'), reverse=reverse)
            for page, book in sorted_dict:
                print(book)