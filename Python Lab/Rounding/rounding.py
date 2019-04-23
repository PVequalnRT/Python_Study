"""
반올림 함수 만들기
"""

#임의의 실수 입력받기

float_num = float(input("임의의 실수를 입력해주세요 :"))

#float_num이 올림을 해야할 지 내림을 해야할지 결정

num = int(float_num)  #판단을 위한 임의의 변수 num 선언 및 초기화
if 2*num < int(2*float_num) :   #판단
    num += 1

#함수 처리결과 출력
print(f"{float_num}을 반올림하면 {num}이 됩니다.")
