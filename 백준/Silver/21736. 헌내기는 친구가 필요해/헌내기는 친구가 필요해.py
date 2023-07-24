from sys import stdin
input = stdin.readline
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]


N,M = map(int, input().split())
visited = [[False] * M for _ in range(N)]

A = []
for i in range(N):
    A.append(list( input()))

def bfs(ix,iy):
    queue = deque()
    queue.append((ix, iy))
    visited[ix][iy] = True
    num = 0

    while queue:
        now = queue.popleft()
        if A[now[0]][now[1]] == "P":
            num +=1
        for j in range(4):
            x = now[0] + dx[j]
            y = now[1] + dy[j]

            if x >= 0 and y >= 0 and x < N and y < M:
                if A[x][y] !=  "X" and not visited[x][y]:
                    visited[x][y] = True
                    queue.append((x, y))

    return num

def find_indexes_2d(arr, target_char):
    indexes = []
    for row_idx, row in enumerate(arr):
        for col_idx, char in enumerate(row):
            if char == target_char:
                indexes.append((row_idx, col_idx))
    return indexes

indexes_of_I = find_indexes_2d(A, "I")
x = indexes_of_I[0][0]
y = indexes_of_I[0][1]
# print(indexes_of_I[0][0],indexes_of_I[0][1])
numm = bfs(x, y)


if numm > 0:
    print(numm)
else:
    print("TT")

