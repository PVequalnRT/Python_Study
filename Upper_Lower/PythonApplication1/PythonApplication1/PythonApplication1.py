String = input("문자열을 입력하시면 대소문자를 바꿔서 출력 됩니다.\n문자를 입력해 주세요 :")

temp = list(String)
temp2 = list()

for tm in temp:
    if tm == " ":
        temp2.append(tm)
    else :
        tm = ord(tm)
        if tm >= 65 and tm <= 90:
            tm += 32
            temp2.append(chr(tm))
        elif tm >= 97 and tm <= 122:
            tm -= 32
            temp2.append(chr(tm))

for i in range(len(temp2)):
    print(temp2[i], end='')