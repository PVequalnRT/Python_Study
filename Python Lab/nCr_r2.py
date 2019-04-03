#nCr을 한 번에 처리하기
#최대한 루프의 횟수를 줄이자.

def nCr(n,r):
    f_result = 1
    l_result = 1
    i = n
    
    #n! / r! 구하기
    while i > r :
        f_result *= i
        i -= 1

    #(n-r)! 구하기
    i = n-r
    while i>0:
        l_result *= i
        i -= 1

    return int(f_result/l_result)


n = int(input("n을 입력해주세요 :"))
r = int(input("r을 입력해주세요 :"))

print(nCr(n,r))

