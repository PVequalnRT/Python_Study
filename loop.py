import time

s_time = time.time()

i = 0
t = 1
b = 1000000

sumnum = 0
while i <  b:
    i += 1
    sumnum += i

print(sumnum)
print(time.time() - s_time)


s_time = time.time()

sumnum = (t+b)*(b-t+1)/2

print(sumnum)
print(time.time() - s_time)
