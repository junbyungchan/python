class Account:
    """
    은행계좌 클래스
    field(데이터): 계좌번호(accountno), 잔액(balance)
    method(기능): 입금(deposit), 출금(withdraw), 이체(transfer)
    """


    def __init__(self,accountno,balance):
        self.accountno = accountno
        self.balance = balance
        # isinstance(balance,int) # balance 가 int 타입이면 True 아니면 False
        # if not isinstance(balance, int) and \  ## --> \ 문자이 끝나지 않았음을 명시해준다.
        #     not isinstance(balance,float):
        #     raise TypeError('')
        # try:
        #     temp = balance + 1
        # except Exception:
        #     raise TypeError()
    def __repr__(self):
        return f'Account(account no.: {self.accountno},balance : {self.balance}'

    def deposit(self,price): # 양수만 입금해주어야한다.
        # if price<0:
        #     raise ValueError('입금 금액은 0보다 크거나 같아야합니다.')
        self.balance += price
        print(f'입금 후 계좌의 잔액은 {self.balance}원 입니다.')



    def withdraw(self,price):
        # if price>0:
        if self.balance >= price:
           self.balance -= price
           print(f'출금 후 계좌의 잔액은 {self.balance}원 입니다.')
        else:
           print('잔액이 부족합니다.')
        # else:
        #     raise ValueError('잔액이 부족합니다.')

    def tranfer(self,other):
        # 계좌번호 입력
        print('계좌 번호를 입력해주세요:')
        inputaccountno = int(input())
        if other.accountno == inputaccountno:
            # 보낼 금액 입력
            print('보내실 금액을 입력해주세요:')
            price = int(input())
            if self.balance >= price:
                # 잔액
                self.balance -= price
                # print문
                print(f'보내실 계좌번호는 {other.accountno}입니다.')
                print(f'이체 금액은 {price}원 입니다.')
                print(f'이체 후 전병찬님 계좌 잔액은 {self.balance}원 입니다.')
                other.balance += price
            else:
                print('잔액 부족')
        else:
            print('계좌번호를 다시 확인해주세요.')
    # 강사님 답안
    def transfer1(self,other,price):
        """
        계좌 이체 기능. 내 계좌에서 price를 출금해서 상대방(other) 계좌에 입금.

        :param other: 이체할 상대방 계좌(Account 클래스 객체)
        :param price: 이체할 금액(숫자 타입)
        :return: None
        """
        self.withdraw(price) # 내 계좌에서 출금
        other.deposit(price) # 상대방 계좌에 입금





if __name__=='__main__':
    account1 = Account(466402,1000)
    account1.deposit(1000)
    account1.deposit(1000)
    account1.withdraw(1000)
    print(account1.balance)
    account2 = Account(434543,10000)
    account1.tranfer(account2)
    account1.transfer1(account2,1000)