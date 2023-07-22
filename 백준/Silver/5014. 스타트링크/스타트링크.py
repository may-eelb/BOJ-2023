
from collections import deque
F, S, G, U , D = map(int, input().split())
dx = [U, -D]

# F : 최고층
# S : 현재 층
# G : target 층
# U : 위 버튼
# D : 아래 버튼


def BFS(start):
    queue = deque()
    queue.append(start)
    visited = [-1] * (F + 1)
    visited[start] = 0

    while queue:
        v = queue.popleft()
        if v == G:
            return visited[v]

        for j in range(2):
            x = v + dx[j]

            if 0 < x <= F and visited[x] == -1:
                queue.append(x)
                visited[x] = visited[v] + 1

    return "use the stairs"

print(BFS(S))
