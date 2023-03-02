import re
custlist=[]
page=-1


while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''')  

    if choice=="I":
        # 2. 입력(I)
        # dictionary로 각 키의 값을 받고 빈 리스트에 채워나간다
        # 성별(sex) : M, m, F, f로만 입력 가능
        # -> 소문자로 입력하는 경우 대문자로 자동 변환
        # -> sex 값이 M 또는 F가 아닐 경우 다시 입력
        # 이메일(email) : 입력값 내 '@'가 반드시 있어야 함
        # -> 정규표현식 사용
        # -> re를 import 하여 이메일 입력값 내 '@' 존재 여부 파악
        # -> 없는 경우 '@'를 포함하라는 문구와 함께 재입력 하도록 함
        # 출생년도(birthyear) : 4자리로 입력 해야
        # -> len 값으로 입력 값의 길이를 구함
        # -> 4자리가 아닐 경우 재입력 하도록 함
        # 출생년도까지 입력이 완료되었을 경우
        # -> 키 값 입력이 완료된 customer 딕셔너리를 custlist 리스트에 추가(append)한다
        # -> 고객 정보가 새로 입력 되었으므로 page 값에 1을 더한다
        
        name = input('이름을 입력해주세요 >>> ')

        while True:
            gender = input('성별(sex)를 남자(M), 여자(F) 입력하세요 >>> ')
            if gender == 'M':
                break
            elif gender == 'm':
                gender = 'M'
                break
            elif gender == 'F':
                break
            elif gender == 'f':
                gender = 'F'
                break
            else:
                print('성별을 잘못 입력하셨습니다. 다시입력해주세요')

        while True:
            email = input('이메일주소를 입력해주세요 >>> ')
            p = re.compile('[a-zA-Z][0-9][@][a_zA-z][0-9][.][a-zA-z][0-9]')
            p_email = p.search('@')
            if p_email != 'None':
                break
            else:
                print('@를 포함하는 이메일주소를 다시입력하세요')

        while True:
            birthyear = input('출생년도(4자리)를 입력해주세요 >>> ')
            bir_len = int(len(birthyear))
            if bir_len == 4:
                break
            else:
                print('출생년도가 4자리가 아닙니다 다시입력하세요')

        customer={'name': name,'gender': gender,"email": email,"birthyear": birthyear}
        custlist.append(customer)
        page += 1

        print("고객 정보 입력")
    elif choice=="C":
        # 3. 조회(C, P, N)
        # 인덱스는 0부터 시작하나 페이지는 통상 1부터 시작하므로 페이지 출력시 page+1 값을 반환한다
        index_num = page - 1
        custlist_value = custlist[index_num]
        print('page : ', page, 'name : ', custlist_value.get('name'), 'gender : ', custlist_value.get('gender'), 'email : ', custlist_value.get('email'), 'birthyear : ', custlist_value.get('birthyear'))
        # 이전 페이지 조회(P)의 경우, 첫 번 째 페이지인 상태에서 이전 페이지로 이동이 불가하므로 현재 페이지인 첫 번 째 페이지를 반환
        # 다음 페이지 조회(N)의 경우, 마지막 페이지인 상태에서 다음 페이지로 이동이 불가하므로 현재 페이지인 마지막 페잊이를 반환

        print("현재 고객 정보 조회")
    elif choice == 'P':
        index_num -= 1
        if index_num < 0:
            index_num = 0
        custlist_value = custlist[index_num]
        print('page : ', page, 'name : ', custlist_value.get('name'), 'gender : ', custlist_value.get('gender'), 'email : ', custlist_value.get('email'), 'birthyear : ', custlist_value.get('birthyear'))
        print("이전 고객 정보 조회")
    elif choice == 'N':
        print("다음 고객 정보 조회")
        index_num += 1
        if index_num >= page:
            index_num = page - 1
        custlist_value = custlist[index_num]
        print('page : ', page, 'name : ', custlist_value.get('name'), 'gender : ', custlist_value.get('gender'), 'email : ', custlist_value.get('email'), 'birthyear : ', custlist_value.get('birthyear'))
    elif choice=='D':
        # 4. 삭제(D)
        # unique한 키를 기준으로 삭제정보를 선택한다 -> 여기서는 이메일로 가정
        unique_key = input('삭제할 key를 입력하세요(입력값: name, gender, email, birthyear) >>> ')
        unique_value = input('삭제할 정보를 입력하세요 >>> ')
        # 삭제 성공 여부 변수(delok)
        delok = 0
        # -> 입력한 이메일이 등록된 정보 내에 있을 경우 삭제
        for key in custlist:
            cust_value = key.value()
            for i in range(len(cust_value)):
                if unique_value == cust_value[i]:
                    unique_dic = {unique_key : ''}
                    key.update(unique_dic)
                    print('삭제 성공!')
                    delok = 1
                    break
                    
        if delok == 0:
            print('등록되지 않은 ', unique_key, ' 입니다. ')
        
        # -> 삭제가 성공하면 delok=1 (default 값 0)
        # -> 등록된 정보 내에 없는 이메일일 경우(delok=0) 등록되지 않았다고 출력

        print("고객 정보 삭제")
    elif choice=="U": 
        # 5. unique한 키를 기준으로 수정정보를 선택한다 -> 여기서는 이메일로 가정
        unique_key = input('수정할 key를 입력하세요(입력값: name, gender, email, birthyear) >>> ')
        unique_value = input('수정하기전 기존 정보를 입력하세요 >>> ')
        # 입력한 이메일과 일치하는 고객 정보의 인덱스를 idx에 입력
        idx = -1
        idx_num = -1
        # -> idx의 default 값은 -1
        for key in custlist:
            idx_num += 1
            cust_value = key.value()
            for i in range(len(cust_value)):
                if unique_value == cust_value[i]:
                    unique_value2 = input('수정할 정보를 입력하세요 >>> ')
                    unique_dic = {unique_key : unique_value2}
                    key.update(unique_dic)
                    idx = idx_num
                    print('수정 성공!')
                    while True:
                        menu2 = input('추가로 수정할 정보 선택(입력값 : name, gender, email, birthyear) 나가기(exit) >>> ')
                        if menu2 == 'name':
                            menu2_value = input('수정할 정보를 입력하세요 >>> ')
                            unique_dic = {menu2 : menu2_value}
                            key.update(unique_dic)
                        elif menu2 == 'gender':
                            menu2_value = input('수정할 정보를 입력하세요 >>> ')
                            unique_dic = {menu2 : menu2_value}
                            key.update(unique_dic)
                        elif menu2 == 'email':
                            menu2_value = input('수정할 정보를 입력하세요 >>> ')
                            unique_dic = {menu2 : menu2_value}
                            key.update(unique_dic)
                        elif menu2 == 'birthyear':
                            menu2_value = input('수정할 정보를 입력하세요 >>> ')
                            unique_dic = {menu2 : menu2_value}
                            key.update(unique_dic)
                        elif menu2 == 'exit':
                            print('수정 종료!')
                            break
                        else:
                            print('잘못입력하셨습니다.')
                    break
        if idx == -1:
            print('등록되지않았습니다. ')
        # -> 일치 여부 확인 후에도 idx가 -1일 경우 등록되지 않았다고 출력
        # 이메일 외에 이름, 성별, 출생년도 중 수정할 정보 선택
        # 수정할 정보 선택 후 수정할 내용 입력
        # 수정하고픈 변수가 없는 경우 exit 입력 시 수정창 종료
        print("고객 정보 수정")
    elif choice=="Q":
        # 6. 종료(Q)
        # 맨처음 while 반복문을 나간다 -> break
        print("프로그램 종료")
        break