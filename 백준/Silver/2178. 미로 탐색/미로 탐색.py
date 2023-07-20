from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

N, M = map(int, input().split())
#A = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

A = []
for i in range(N):
    A.append(list(map(int, input())))

def bfs(ix,iy):
    queue = deque()
    queue.append((ix, iy))
    visited[ix][iy] = True

    while queue:
        now = queue.popleft()
        for j in range(4):
            x = now[0] + dx[j]
            y = now[1] + dy[j]

            if x >= 0 and y >= 0 and x < N and y < M:
                if A[x][y] !=  0 and not visited[x][y]:
                    visited[x][y] = True
                    A[x][y] = A[now[0]][now[1]] + 1
                    queue.append((x, y))

bfs(0,0)
print(A[N-1][M-1])