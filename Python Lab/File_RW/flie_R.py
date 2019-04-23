file = open("character.txt", "r")

name = input("전투력을 검색할 캐릭터 이름 입력 : ") + "\n"

while True :
    if name == file.readline() :
        print(file.readline())
        break
file.close()
