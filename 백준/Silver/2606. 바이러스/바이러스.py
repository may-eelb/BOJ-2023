
N = int(input())
M = int(input())

graph = [ [] for _ in range(N+1)]

for i in range (M):
    a, b = (map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N +1)
cnt = -1

def DFS(v):
    visited[v] = 1
    global cnt
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

DFS(1)
print(cnt)
