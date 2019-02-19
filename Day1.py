"""
#평균 구하기

korean = 80
english = 75
math = 55

sum = korean + english + math
average = sum / 3

print(average)
#"""

"""
#홀짝 판별

num = 11
if num%2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

#"""

"""
#문자열 종류

print("Hello World!") #큰따옴표
print('python is fun')#작은따옴표
print(""Life is too short"")#큰따옴표3개
print('''you need python''')#작은따옴표3

#"""

"""
#문자열 길이 구하기

a = "hello!"
print(len(a))

#"""

"""
#인덱스 및 슬라이싱 기능 연습

a = "Hello World!"
print(a[0]+a[1])
print(a[0:6])
print(a[:6])
print(a[6:])
print(a[0:-7])

#"""

"""
#input함수는 항상 문자열로 받으니 int로 형변환을 해줘야한다.
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)

print("두 수의 합은 %s 입니다" % total)
#"""

"""
#코딩도장 문제풀이

num = input("숫자를 입력해주세요 :")
i = len(num)
a = 0
total = 0

while a < i:
    total = total + int(num[a])
    a = a + 1

print("\n\n각자리 숫자의 총합은",total," 입니다.")
#"""


"""
print(sum(map(int, input("숫자를 입력하세요 : "))))
"""
