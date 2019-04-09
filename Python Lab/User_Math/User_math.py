#User Math 클래스 선언
class user_math(object):

    def __init__(self,num):  #함수 초기화
        self.num = num

    def mul_2(self):
        if self.num % 2 == 0 :
            print("2의 배수입니다.")
        else :
            print("2의 배수가 아닙니다.")

    def mul_3(self):
        if self.num % 3 == 0 :
            print("3의 배수입니다.")
        else :
            print("3의 배수가 아닙니다.")

    def prime_num(self):
        num1 = 2
        """
        if self.num % num1 == 0 :
            print("소수가 아닙니다.")
            return 0

        num1 = 3
        """
        while num1 < self.num:
            if self.num % num1 == 0:
                print("소수가 아닙니다.")
                break
            
            elif num1 == (self.num - 1):
                print("소수입니다.")
                break

            num1 += 1



if __name__ == '__main__' :   #모듈 소스코드 오류 없는지 검사
    print("정상 작동")
