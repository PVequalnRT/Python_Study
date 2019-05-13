from os import system
f = open('sample.txt', 'r')
data = f.readlines()
f.close()


total = 0

for num in data:
    total += int(num)

total = total / len(data)

f = open('result.txt', 'w')
f.write(str(total))
f.close()

system('pause')
