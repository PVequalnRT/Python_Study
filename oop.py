#How to use oop (object oriented project)

class Cal(object) :
    def __init__(self, num1, num2) :
        self.num1 = num1
        self.num2 = num2

    def add(self) :
        return self.num1 + self.num2

    def subtract(self) :
        return self.num1 - self.num2


num1 = int(input("첫 번째 숫자를 입력하세요."))
num2 = int(input("두 번째 숫자를 입력하세요."))

c = Cal(num1, num2)
print(c.add())
print(c.subtract())
