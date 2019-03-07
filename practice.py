#개인적인 연습
#1. 반복문 이용해 1~100까지의 수 합
import time

start = time.time()
i = 0
sum_num = 0

while i < 100:
    i += 1
    sum_num += i

print(sum_num)
end = time.time()

print(end - start)

print("\n\n\n")

start = time.time()
j = 1
i = 100

sum_num = int((i + j)*(i-j+1)/2)

print(sum_num)
end = time.time()

print(end - start)

