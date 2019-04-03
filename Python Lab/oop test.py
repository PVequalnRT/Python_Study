#바로 클래스를 함수로 만드는 것은 안된다.

class test(object):
    def __init__(self, num):
        self.num = num

    def twice(self):
        return self.num * 2

num = int(input("두 배로 만들 숫자를 입력하세요 : "))

#print(test.twice(num))




