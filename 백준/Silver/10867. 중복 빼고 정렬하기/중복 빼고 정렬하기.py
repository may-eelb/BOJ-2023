from sys import stdin
input = stdin.readline

N = int(input())

my_list = list(map(int, input().split()))

temp = set(my_list)
t = sorted(temp)
print(*t)
