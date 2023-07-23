

from sys import stdin
input = stdin.readline

N = int(input())
list = list(map(int, input().split()))

list.sort()
min = 0
for i in range( N):
    min += list[N-1-i] * (i+1)

print(min)