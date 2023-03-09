# 원금과 이자율을 입력하면 
# CMA 이자를 계산해서 경과시간 후에 얼마의 돈이 생기는지 알려주는 프로그램

# 원금입력
n = int(input("원금 : "))
print()

# 이자율 입력 받고, 100으로 나눔
r = float(input("이자율 : "))/100
print()

# 경과 기관 입력 받음, 영업일 기준으로 입력 받기
l = int(input("경과 영업일 :"))
print()

# 하루에 받는 이자 계산, 계산후 자산이 늘어나는 것을 고려해 1 더해줌.
realR = r * 0.846 / 365 + 1


# 1. 무한루프 방식으로 구현
i = 0
result = n
while (i<l):
    result *= realR
    i += 1

print(l,"영업일 경과 후 잔액 : ", result)

# 2. 등비수열로 구현
result = n * (realR ** l)

print(l,"영업일 경과 후 잔액 : ", result)


# 일복리와 그냥 연복리를 알고 싶어서 구현
# 일복리
print(l,"일 경과 후 잔액(일복리) : ", result)
print(l,"일 경과 후 잔액(년리) : ", n*((r*0.846+1)**(l/365)))
print("일복리와 년이자 차이 = ", result - n*((r*0.846+1)**(l/365)))