import os
with open('f.txt', 'a', encoding = 'UTF-8') as f:
    f.write('나는 행복하지 않았다!\n')

with open('f.txt', 'r', encoding = 'UTF-8') as f:
    while(1):
        t = f.readline()
        if not t: break
        print(t, end = '')

os.system('pause')
