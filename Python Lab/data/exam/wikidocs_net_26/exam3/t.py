f = open('abc.txt', 'r')
lines = f.readlines()
lines.reverse()
f.close()

f = open('abc.txt', 'w')
for line in lines :
    f.write(line)

f.close()
