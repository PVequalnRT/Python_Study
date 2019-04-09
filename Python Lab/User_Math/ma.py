from User_math import user_math
import os
import time

class user_math2(user_math) :

    def __init__(self, num) :
        super().__init__(num)

    def mul_3_new(self):  #3의 배수 구하는 다른 방법
        return 0

while True :
    a = """사용하시고 싶은 기능을 선택하세요.

1. 2의 배수 판독
2. 3의 배수 판독
3. 소수 판별
4. 종료"""

    print(a)
    menu = int(input())

    print(f"선택하신 기능은 {menu}번입니다.")
    a = user_math(int(input("정수를 입력해주세요 :")))

    if menu == 1:
        a.mul_2()
        print("")

    elif menu == 2:
        a.mul_3()
        print("")
    
    elif menu == 3:
        st = time.time()
        a.prime_num()
        print(time.time() - st)
    
    elif menu == 4:
        print("종료합니다.")
        print("")
        break

    else :
        print("다시 입력해주세요.")
        print("")

    input("처음으로 되돌아갑니다.")
    os.system('cls')
