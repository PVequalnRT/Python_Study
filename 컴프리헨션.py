a = [ (x, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피']]

for b in a:
    print(b)

a = [ 2*x for x in range(1, 10+1) ]
for b in a:
    print(b)


a = [x for x in range(1, 10+1) if x % 2 == 0]
for b in a:
    print(b)

a = [ x for x in range(10) if x < 5 if x % 2 == 0 ]
for b in a:
    print(b)
