"""
클래스(class):
프로그램에서 만들려고 하는 대상(객체)이 가져야 할
속성(데이터)과 기능(함수)을 묶은 "데이터 타입"

클래스 = 메소드 + 필드

메소드(method): 클래스가 가지고 있는 함수
필드(field): 클래스가 가지고 있는 데이터(변수)
"""

# TV 소프트웨어 작성
# TV 속성(데이터): 채널, 음량, 전원 ( 필드)
# TV 기능: 채널 변경, 음량 변경, 전원 on/off ( 메소드)

# 클래스 설계(정의)
class BasicTv:
    """
    BasicTv 클래스
    """
    # 생성자가 호출됐을 때 실행되는 특별한 메소드(함수) : __init__ 아랫작대기2개다.
    # self의 의미: 주소값(객체가 생성 되어 확보된 메모리의 주소)

    # 클래스 내부에서 선언하는 변수 : field
    max_channel, min_channel = 5, 0
    max_volume, min_volume = 5, 0
    def __init__(self,power,channel,volume):
        print('BasicTv 생성자 호출')
        # TV의 속성들
        self.power = power
        self.channel = channel
        self.volume = volume


    # 클래스 내부에서 정의하는 함수 : 메소드( 메소드는 항상 첫번째 파라미터는 self)
    def powerOnOff(self):
        if self.power: # TV가 켜져있을 때
            self.power = False
            print('TV OFF')
        else:  # TV가 꺼져있을 때
            self.power = True
            print('TV ON')


    def channelUp(self): # channel 올리기

        if self.power == True:
            if self.channel < self.max_channel :
                # 현재 채널 값이 채널의 최댓값보다 작으면 +1
                self.channel += 1
            else :
                # 현재 채널 값이 채널 최댓값과 같으면 0로 순환
                self.channel = self.min_channel
            print('Channel:', self.channel)


    def channelDown(self): # channel 내리기
        if self.power == True:
            if self.channel > self.min_channel:
                # 현재 채널이 채널 최솟값보다 큰 경우에만 -1
                self.channel -= 1
            else:
                # 현재 채널이 최솟값인 경우는 채널 최댓값으로 순환
                self.channel = self.max_channel
            print('Channel:',self.channel)


    def volumeUp(self): # volume 올리기
        # TV가 켜져 있는 경우에만 음량 +1
        if self.power == True:
            if self.volume < self.max_volume:
                # 현재 음량이 음량 최댓값보다 작은 경우 +1
                self.volume += 1
                print('Volume:',self.volume)
            else: # 음량이 최댓값이면 MAX라고 띄우고 볼륨을 유지한다.
                print('Volume: MAX')



    def volumeDown(self): # volume 내리기
        if self.power == True:
            if self.volume > self.min_volume:
                # 현재 음량이 음량 최솟값보다 큰 경우 -1
                self.volume -= 1
                print('Volume:',self.volume)
            else: # 음량이 최솟값이면 음소거라고 띄우고 볼륨을 유지한다.
                print('Volume: 음소거')
# ------------------------------------------

if __name__ == '__main__':
    tv1 = BasicTv(False,0,0)
    print('전원상태:',tv1.power)
    tv1.powerOnOff() #TV를 켬
    tv1.channelUp()
    tv1.channelUp()
    tv1.channelUp()
    tv1.channelUp()
    tv1.channelUp()
    tv1.channelUp()
    for _ in range(10):
        tv1.volumeUp()
    for _ in range(12):
        tv1.volumeDown()





#-------------------------------------------
# 클래스의 객체(인스턴스)를 생성해서 변수에 저장
# 생성자(constructor) 호출 -> 객체(object) 생성
# tv1 = BasicTv(power=False,channel=0,volume=0) # 객체 생성
# print(tv1)
# print(tv1.power)
# tv1.powerOnOff() # TV 켬
# tv1.channelUp()
# tv1.channelUp()
# tv1.channelDown()
# tv1.powerOnOff() # TV 끔
# tv1.powerOnOff() # TV 다시 켬
# print(tv1.channel)
# tv1.volumeUp()
# tv1.volumeUp()
# tv1.volumeUp()
# tv1.volumeUp()
# tv1.volumeUp()
# tv1.volumeDown()
# # tv1.powerOnOff()
# print(tv1.channel,tv1.volume)
# # 객체.메소드() -> self값을 주지 않아도 객체의 주소값을 가지고 있기 때문에
# # 안써줘도 된다.
# tv2 = BasicTv(True,5,99) # 생성자 호출
# tv2.channelUp()
# tv2.volumeUp()
# tv2.volumeUp()
# tv2.volumeUp()
# tv2.volumeUp()
# tv2.volumeUp()
# tv2.volumeUp()
# tv2.powerOnOff()
# tv2.volumeDown()
# tv2.volumeDown()
# tv2.volumeDown()
# tv2.volumeDown()
# tv2.volumeDown()
# tv2.volumeUp()
# tv2.powerOnOff()
# tv2.channelUp()
# tv2.channelUp()
# tv2.channelUp()
# tv2.channelUp()
# tv2.channelUp()
# tv2.channelUp()
# tv2.channelUp()
# tv2.channelUp()
# tv2.channelUp()
# tv2.channelDown()
# tv2.channelDown()
# tv2.channelDown()
# tv2.channelDown()
# tv2.channelDown()
# tv2.channelDown()
# tv2.channelDown()
# tv2.channelDown()
# tv2.channelDown()

