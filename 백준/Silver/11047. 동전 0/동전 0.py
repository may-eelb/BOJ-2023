from sys import stdin
from collections import deque
input = stdin.readline

N, A = map(int, input().split())
list = deque()
for i in range(N):
    list.append(int(input()))
num = 0

while list and A > 0:
    x = list.pop()
    if ( A // x > 0):
        num += A // x
        A = A % x


print(num)