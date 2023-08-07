from sys import stdin
from collections import deque
input = stdin.readline

n = int(input().strip())
k = int(input())
apple = []
for _ in range(n):
    apple.append([0] * n)

for _ in range(k):
    y, x = map(int, input().split())
    apple[y - 1][x - 1] = 1

L = int(input())
times = {}
for i in range(L):
    X, C = input().split()
    times[int(X)] = C

# 위부터 시계방향 90도
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


direction = 1
time = 1
y, x = 0, 0
snake = deque([[y,x]])
apple[y][x] = 2

def direction_change(d, c):
    # d : 현재 방향 ( 처음엔 오른쪽 , index = 1)
    if c == "L": # 왼쪽으로 90도 1 -> 0, 0 -> 3, 3 -> 2, 2->1
        d = (d - 1) % 4
    else:  # 오른쪽으로 90도 1 -> 2, 2-> 3, 3-> 0, 0-> 1
        d = (d + 1) % 4

    return d

while True:
    y, x = y + dy[direction], x + dx[direction]
    if 0 <= y < n and 0 <= x < n and apple[y][x] != 2:
        if not apple[y][x] == 1: # 사과가 없다면
            delY, delX = snake.popleft()  # 꼬리부분을 뱀의 스택에서 비운다
            apple[delY][delX] = 0 # 전체 맵에서도 2 -> 0 으로 변경
        # 벽에 안닿고 자기자신에 안닿는다면
        apple[y][x] = 2 # 뱀의 머리
        snake.append([y, x])
        if time in times.keys():
            direction = direction_change(direction, times[time])
        time += 1
    else:
        break

print(time)




