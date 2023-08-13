from sys import stdin
from collections import deque
input = stdin.readline
n = int(input())


for i in range(n):
    print('*' * (n-i))