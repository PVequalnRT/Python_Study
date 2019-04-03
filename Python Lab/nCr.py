#팩토리얼 구현
def factorial(num):
    i = num
    result = 1
    while i > 0:
        result *= i
        i -= 1
    return result


#사용자에게 nCr 입력 받음
n = int(input("총 개수를 입력해주세요 : "))
r = int(input("뽑을 개수를 입력해주세요 :"))

if r>n :
    print("n은 r보다 크거나 같아야 합니다.")
else :
    result = int(factorial(n)/(factorial(r)*factorial(n-r)))
    print(result)
