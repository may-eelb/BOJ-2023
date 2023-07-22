from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
visited = [0] * 1001
graph = [[0 for _ in range(1001)] for _ in range(1001)]
num = 0
def BFS(v):
    #print("현재 BFS")
    global num
    num += 1

    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        x = queue.popleft()
        for j in range(1, N+1):
            if graph[x][j] == 1 and visited[j] == 0:
                #print(f'{x} 에서 {j}')
                queue.append(j)
                visited[j] = 1


for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


for k in range(1, N+1):
    if not visited[k]:
        BFS(k)

print(num)
