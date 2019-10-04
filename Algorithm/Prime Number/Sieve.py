#Sieve Of Eratosthenes
import math

def is_prime_number_sieve(element):
    num_list = range(2, element + 1)
    for i in range(2,round(math.sqrt(element)) + 1):
        j = 0
        while j  < len(num_list):
            if num_list[j] == i:
                pass
            elif num_list[j] == 0 :
                pass
            elif num_list[j] % i == 0:
                num_list[j] = 0
    return num_list  

print(is_prime_number_sieve(10))