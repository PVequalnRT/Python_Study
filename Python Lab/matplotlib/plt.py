import matplotlib.pyplot as plt

temp = plt
a = range(101)

b = list()

for temp2 in a:
    
    b.append(2 ** temp2)

temp.plot(a,b)
temp.show()
