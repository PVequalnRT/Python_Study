import time

def is_prime_number(target):
    if target == 1:
        return False
    elif target == 2 or target == 3:
        return True
    elif target % 2 == 0:
        return False
    else:
        i = 3
        while i < target:
            if target % i == 0:
                return False
            else:
                i += 2
        return True

def count_prime_number(number):  #count prime number small then input number
    count = 0
    for i in range(1, number + 1):
        if is_prime_number(i):
            count += 1
    return count
stime = time.time()
print(count_prime_number(100000))
print(time.time() - stime)