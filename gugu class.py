#gugu class + for문 연습
"""
for i in [1,2,3,4,5,6,7,8,9]:
    for j in [2,3,4,5]:
        print("%d x %d = %2d   " %(j,i,j*i), end='')
    print("")

print("")

for i in [1,2,3,4,5,6,7,8,9]:
    for j in [6,7,8,9]:
        print("%d x %d = %2d   " %(j,i,j*i), end='')
    print("")
"""

def pri(n):
    for i in [1,2,3,4,5,6,7,8,9] :
        j = n
        while j <= (n+3):
            print("%d x %d = %2d   " %(j,i,j*i), end='')
            j += 1
        print("")
        

pri(2)
print("", end='\n\n')
pri(6)
