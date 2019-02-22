#리스트

"""
#리스트 기초

a = [1,2,3]
print(a)
print(a[1])
print(a[-1] + a[2])

a = [1,2,3,['a','b', 'c']]
print(a)
print(a[3])
print(a[3][1])  #삼중까지도 가능.... 근데 쓸 일은 거의 없을듯
#"""

"""
#리스트 슬라이싱

a = [1,2,3,4,5]
print(a[:2])

a = [1,2,3,['a','b','c'],4,5]
print(a[0:4])
print(a[3][0:2])
#"""

"""
#리스트 연산

a = [1,2,3]
b = [4,5,6]

print(a+b)
print(a*2)
print(len(a+b))

print(str(a[1]) + "Hello!")
#"""

#"""
#리스트 수정과 삭제

a = list() #비어있는 리스트 생성
a = [1,2,3]
a[2] = 4

print(a)

del a[2] #리스트 요소 삭제
print(a)

a = [1,2,3,4,5,6,7,8,9,10]
del a[6:] #삭제 명령어를 슬라이싱 기능과 결부
print(a)

a = [1,2]
a.append(3) #리스트에 삽입
print(a)
a.append([4,5])
print(a)

print("\n")

a = [1,6,2,4,2]
a.sort() #리스트 요소값을 오름차순으로 정렬
print(a)

a.reverse() #리스트 요소값 역순 정렬
print(a)

print("\n")

a = [1,2,3]
print(a.index(2)) #특정 요소값을 찾아 그 위치를 반환
print(a.index(1))

a.insert(1,2.5) #(a, b) a위치에 b를 삽입
a.insert(4,[5,6])
print(a)

print("\n")

a.remove(2.5) #특정 요소값 제거
a[3].remove(5)
print(a)

print("\n")

a = [1,2,3]
print(a.pop()) #맨 끝자리 값 출력후 리스트에서 삭제
print(a.pop(0)) #특정 위치에 있는 값을 출력하고 그 값을 리스트에서 삭제
print(a)


print("\n")

a = [1,2,2,3,3,3,4,5,2]
print(a.count(2)) #리스트 내의 특정 값 개수 세기
a.extend([9,10]) #리스트에 특정 값 추가, 이때 리스트 요소로 들어감
print(a)
a += [11,12]
print(a)
#"""
