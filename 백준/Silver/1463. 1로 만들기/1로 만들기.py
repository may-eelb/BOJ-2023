
from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
list = []
def BFS(start):
    queue = deque()
    queue.append(start)
    visited = [-1] * (1000000 + 1)
    visited[start] = 0

    while queue:
        v = queue.popleft()
        if v == 1:
            return visited[v]

        if v%3 == 0 and visited[v//3] == -1:
            queue.append(v//3)
            #print(f'1큐에 쌓이는 {v // 2}')
            visited[v//3] = visited[v] + 1

        elif v%2==0 and visited[v//2] == -1:
            queue.append(v // 2)
            #print(f'2큐에 쌓이는 {v//2}')
            visited[v // 2] = visited[v] + 1


        if v-1 > -1 and visited[v-1] == -1:
            queue.append(v -1)
            #print(f'큐에 쌓이는 {v -1 }')
            visited[v -1] = visited[v] + 1
def BFS2(start):
    queue = deque()
    queue.append(start)
    visited = [-1] * (1000000 + 1)
    visited[start] = 0

    while queue:
        v = queue.popleft()
        if v == 1:
            return visited[v]

        if  v % 2 == 0 and visited[v // 2] == -1:
            queue.append(v // 2)
            # print(f'2큐에 쌓이는 {v//2}')
            visited[v // 2] = visited[v] + 1

        elif v%3 == 0 and visited[v//3] == -1:
            queue.append(v//3)
            #print(f'1큐에 쌓이는 {v // 2}')
            visited[v//3] = visited[v] + 1


        if v-1 > -1 and visited[v-1] == -1:
            queue.append(v -1)
            #print(f'큐에 쌓이는 {v -1 }')
            visited[v -1] = visited[v] + 1


temp1 = BFS(N)
temp2 = BFS2(N)
print(min(temp1, temp2))
