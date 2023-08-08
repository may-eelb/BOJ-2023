from sys import stdin
from collections import deque
input = stdin.readline

a, b = input().strip().split()
# 반복횟수 len(b) - len(a) - 1

minv = len(a)
for i in range(len(b) - len(a) + 1):
    cnt = 0
    #print(f' 현재 i { i}')
    for j in range(i, len(a) + i ):
        #print(a[j - i], b[j ])
        if a[j - i] != b[j ]:

            cnt +=1
    #print(f' 현재 i : {i} 에서 {cnt}')

    minv = min(cnt, minv)

print(minv)