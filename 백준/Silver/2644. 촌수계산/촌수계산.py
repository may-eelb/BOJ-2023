from collections import deque

N = int(input())
A, B = map(int,input().split())
M = int(input())

mlist = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    mlist[a].append(b)
    mlist[b].append(a)

visited = [0] * (N+1)
num = 0
result = -1

def DFS(v, cnt):
    global result
    cnt+=1
    visited[v] = 1
    if v == B:
        result = cnt-1
    for i in mlist[v]:
        if not visited[i]:
            DFS(i, cnt)

DFS(A, 0)

print(result)