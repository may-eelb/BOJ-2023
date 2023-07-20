from collections import deque

N, M = map(int, input().split())
distance = [0] * (100001)

def bfs():
    q =deque()
    q.append(N)


    while q:

        x = q.popleft()
        dx = [-1, 1, x]
        if x == M:
            print(distance[x])
            break
        for i in dx:
            if 0 <= x + i <= 100000 and distance[x+i] == 0:
                distance[x+i] = distance[x] + 1
                q.append(x+i)

bfs()