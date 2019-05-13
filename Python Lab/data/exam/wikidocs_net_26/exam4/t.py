f = open('test.txt' , 'r')
data = f.read()
f.close()

data = data.replace('java', 'python')

f = open('test.txt', 'w')
f.write(data)
f.close()
