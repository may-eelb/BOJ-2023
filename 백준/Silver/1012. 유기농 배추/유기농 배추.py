from collections import deque


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS(x, y):
    queue = deque([(x,y)])
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0

T = int(input())
#
for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0 for _ in range(N)] for _ in range(M)]
    cnt = 0

    for _ in range(K):
        a, b = map(int, input().split())

        graph[a][b] = 1


    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                BFS(i,j)  # 한덩이 다돌고 cnt + 1
                cnt += 1

    print(cnt)
