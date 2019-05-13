#사용자로부터 문자열을 입력받아
#대문자 -> 소문자
#소문자 -> 대문자
#그외 문자는 그대로 바꿔서 다시 문자열로 출력하는 프로그램
#=====================================================
#객체지향적 구현

#클래스 선언
class stri(object):
    def __init__(self, st):
        self.st = st

    def upper(self):
        result = []
        for t in list(self.st):
            if ord(t) >= 97 and ord(t) <= 122:
                result.append(chr(ord(t) - 32))
            else:
                result.append(t)
        return "".join(result)

    def lower(self):
        result = []
        for t in list(self.st):
            if ord(t) >= 65 and ord(t) <= 90:
                result.append(chr(ord(t) + 32))
            else:
                result.append(t)
        return "".join(result)

    def change(self):
        result = []
        for t in list(self.st):
            if ord(t) >= 97 and ord(t) <= 122:
                result.append(chr(ord(t) - 32))
            elif ord(t) >= 65 and ord(t) <= 90:
                result.append(chr(ord(t) + 32))
            else :
                result.append(t)
        return "".join(result)


#프로그램 시작

#사용자로 부터 입력을 받고 인스턴스 생성
st = stri(input("변환할 영문 문자열을 입력해주세요."))
print(st.change())
print(st.upper())
print(st.lower())
