from collections import deque

N, M, V = map(int, input().split())
graph = [ [0] * (N+1) for _ in range(N+1)]

for i in range (M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1       # 이어져있다면 T

visited1 = [0] * ( N+ 1 )
visited = [0] * ( N+ 1 )
answer = []
def DFS(V):
    visited1[V] = 1
    print(V, end = " ")

    for j in range(1, N+1):
        if graph[V][j] == 1 and visited1[j] == 0:
            visited1[j] = 1
            DFS(j)


def BFS(V):
    q = deque([V])
    visited[V] = 1

    while q:
        V = q.popleft()
        print(V, end = ' ')
        for i in range(N+1):
            if (visited[i] == 0 and graph[V][i] == 1):
                q.append(i)
                visited[i] = 1
DFS(V)
print()
BFS(V)

