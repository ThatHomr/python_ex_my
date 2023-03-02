# 은행 계좌(Account)를 클래스로 작성하시오
class Account:
    
    # 계좌가 계설된 건수
    account_count = 0
    
#     # 클래스 변수를 이용하여 계좌가 개설된 건수를 체크하고 출력하는 클래스함수를 작성합니다.
#    클래스 함수
#    @classmethod
# 	def get_account_num(cls):
# 		pass

    @classmethod
    def get_account_num(cls):
        return Account.account_count

# 아래의 내용은 인스턴스 함수와 변수로 작성합니다.
# 계좌는 이름과 금액을 입력받고, 계좌번호는 자동으로 생성합니다.
    # def __init__(self, bank_name, name, money) -> None:
    #     self.bank_name = bank_name
    #     self.name = name
    #     self.money = money
    #     self.account_num = Account.account_count
    #     self.deposit_count = 1
    #     self.withraw_count = 0
    #     Account.account_count += 1

    def __init__(self, name, balance):
        Account.account_count += 1
        self.account_number = Account.account_count
        self.name = name
        self.balance = balance
        self.total_log = []
        self.deposit_count = 0
        # self.total_log.append(self.balance)

# 입금은 0보다 큰 금액을 입력해야하며 로그에 입금내역을 기록합니다.
# 입금 횟수에 따라 1%의 이자가 지급됩니다.(5회마다)
    # 입금처리
    # def deposit(self, money):
    #     self.deposit_count += 1
    #     self.balance += money
    #     if self.deposit_count % 5 == 0:
    #         self.balance += (0.01 * self.balance)
    #     self.total_log.append(self.balance)
    def deposit(self, amonut):
        if amonut >= 1:
            self.total_log.append(('입금', amonut))
            self.balance += amonut
            self.deposit_count += 1
            print(amonut, '원 입금처리 완료!')
            if self.deposit_count % 5 == 0:
                interest = round(self.balance * 0.01, -1)
                self.balance += interest
                self.total_log.append(('이자', interest))
                print(interest, '원의 이자가 지급되었습니다.')

# 출금은 잔액보다 작거나 같을 경우에 처리됩니다. 로그에 출금 기록을 남깁니다.
    # 출금처리
    # def withdraw(self, amonut):
    #     if self.balance >= amonut:
    #         self.balance -= amonut
    #         self.total_log.append(('출금', amonut))
    #         print(amonut, '원 출금처리 완료!')
    #         print('잔고 : ', self.balance, '원')
    #     else:
    #         print('잔액이 부족합니다.')
    def withdraw(self, amonut):
        if self.balance >= amonut:
            self.total_log.append(('출금', amonut))
            self.balance -= amonut
            print(amonut, '원 출금처리 완료!')
        else:
            print('잔액이 부족합니다.')

# 계좌정보를 출력하는 함수는 예금주, 계좌번호, 잔고를 출력합니다.
    # 계좌정보출력함수
    def displayinfo(self):
        print(self.__str__())

    def __str__(self):
        return f'예금주 :{self.name}, 계좌번호 :{self.account_number}, 잔고 :{self.balance}'

# print(Account.account_count)
print(Account.get_account_num())
a = Account('홍길동', 2000)
a.displayinfo()
a.deposit(5000)
a.displayinfo()
a.withdraw(3000)
a.displayinfo()
print(a.total_log)
