"""
class test(object):
    def __i__(self, num):
        self.num = num

    def twice(self):
        return self.num * 2

a = test(1)
print(a.twice())
#"""

class test(object):
    def __init__(self, num):
        self.num = num

    def twice(self):
        return self.num * 2

num = int(input("두 배로 만들 숫자를 입력하세요 : "))
a = test(num)
print(a.twice())
