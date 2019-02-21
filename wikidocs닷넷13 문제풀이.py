#https://wikidocs.net/13 문제풀이

"""
#문제 1 홍길동의 주민번호는 881120-1068234이다.
#주민등록번호를 연월일부분과 그 뒤 숫자부분으로 나누어 출력

num = "881120-1068234"
a, b = num.split("-")

print(a,b)
#"""

"""
#문제 2 위 주민등록번호에서 성별을 나타내는 숫자를 출력해보자.

pin = "881120-1068234"

print(pin[7])

#"""


"""
#문제 3 a:b:c:d 이 문자열을 a#b#c#d 로 고쳐라. 단 replace함수 사용

a = "a:b:c:d"
a = a.replace(":", "#")

print(a)
#"""


#"""
#문제4 3과 동일하나 split과 join함수 이용

a = "a:b:c:d"
a = a.split(":")
a = "#".join(a)

print(a)

#"""
