#https://wikidocs.net/21  문제 풀이
"""   1에서 1000까지의 자연수 중 3의 배수의 합

a = 0
num = 0

while a<1000:
    a += 1
    if a % 3 == 0:
        num += a
    else :
        continue

print(num)

#"""

#"""
#무한루프로 문제 풀어보기

a = 0
num = 0

while True:
    a += 1
    if a == 1001 :
        break
    elif a%3 == 0:
        num+=a

print(num)

#"""
