from collections import deque

from sys import stdin
input = stdin.readline


N = int(input())

deque1 = deque()

for _ in range(N):
    deque1.append(int(input()))

if (N == 0):
    print(0)

else :

    del_cnt = round(len(deque1) * 0.15 + 0.00000001)

    sortedDe = deque(sorted(deque1))
    for i in range(del_cnt):
        sortedDe.popleft()
        sortedDe.pop()

    print(round(sum(sortedDe) / len(sortedDe) + 0.00000001))

