#사용자로부터 문자열을 입력받아
#대문자 -> 소문자
#소문자 -> 대문자
#그외 문자는 그대로 바꿔서 다시 문자열로 출력하는 프로그램
#=====================================================
#절차지향적 구현


#대문자 -> 소문자 변환 함수
def lower(temp):
    return chr(temp + 32)

#소문자 -> 대문자 변환
def upper(temp):
    return chr(temp - 32)

#사용자로부터 문자열 입력받기
f_str = list(input("변환할 영문 문자열을 입력해 주세요 :"))
result = []

#upper lower 함수 선언 조건 및 루프
for temp in f_str:
    if ord(temp) >= 65 and ord(temp) <= 90:
        result.append(lower(ord(temp)))

    elif ord(temp) > 97 and ord(temp) <= 122:
        result.append(upper(ord(temp)))

    else :
        result.append(temp)

#변환 결과 출력
print("".join(result))
