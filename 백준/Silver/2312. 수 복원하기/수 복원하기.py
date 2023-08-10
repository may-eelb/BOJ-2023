from sys import stdin
from collections import deque
input = stdin.readline
def prime_factoers(n):
    factors = {}
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            if divisor in factors:
                factors[divisor] += 1
            else:
                factors[divisor] = 1
            n //= divisor
        divisor += 1

    return factors


n = int(input())
for _ in range (n):
    target = int(input())
    temp = {}
    temp = prime_factoers(target)
    for key, value in temp.items():
        print(f'{key} {value}')