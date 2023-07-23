
from sys import stdin
input = stdin.readline

N , M = map(int, input().split())
plist = []
for i in range(N):
    plist.append(input().strip())

for j in range(M):
    input_str = input().strip()

    if input_str.isdigit():
        print(plist[int(input_str)-1])

    else:
        print(plist.index(input_str)+1)