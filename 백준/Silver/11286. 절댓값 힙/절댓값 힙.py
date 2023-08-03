from sys import stdin
input = stdin.readline
import heapq

pq = []
n = int(input())
for _ in range (n):
    temp = int(input())
    if temp == 0:
        if pq :
            print(heapq.heappop(pq)[1])
        else :
            print(0)
    else:
        heapq.heappush(pq, (abs(temp), temp ))

