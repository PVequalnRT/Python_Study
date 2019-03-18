"""
#첫 번째. 필요할 때 마다 숫자를 작성해서 만듦

num1 = int(input("첫 번째 숫자를 입력하세요."))
num2 = int(input("두 번째 숫자를 입력하세요."))

print(num1+num2)

num1 = int(input("첫 번째 숫자를 입력하세요."))
num2 = int(input("두 번째 숫자를 입력하세요."))

print(num1-num2)

#매번 줄을 늘려나가기 귀찮다/
#"""


"""
def add(num1, num2) :
    print(num1 + num2)

def subtract(num1,num2):
    print(num1 - num2)


num1 = int(input("첫 번째 숫자를 입력하세요."))
num2 = int(input("두 번째 숫자를 입력하세요."))

add(num1,num2)
subtract(num1,num2)

#이것도 귀찮음. 그래서 클래스를 만들기로 함
#"""


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
