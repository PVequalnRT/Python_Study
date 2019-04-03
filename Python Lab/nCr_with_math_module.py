import math

#사용자에게 nCr 입력 받음
n = int(input("총 개수를 입력해주세요 : "))
r = int(input("뽑을 개수를 입력해주세요 :"))

if r>n :
    print("n은 r보다 크거나 같아야 합니다.")
else :
    result = int(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))
    print(result)
