from sys import stdin
input = stdin.readline


# 슬라이딩 윈도우
n = int(input())
m = int(input())
my_list = list(map(int, input().split()))

my_list.sort()

i = 0
j = n-1
count = 0
while i < j:
    if my_list[i] + my_list[j] < m:
        i += 1
    elif my_list[i] + my_list[j] > m:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)