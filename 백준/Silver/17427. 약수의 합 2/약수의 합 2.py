from sys import stdin
input = stdin.readline

N = int(input())
sum = 0

for i in range ( 1, N+1):
    # i 배수의 개수 -> 몫
    sum += ( N// i) * i

print(sum)