from sys import stdin
input = stdin.readline


n = int(input())
temp = list(map(int, input().split()))
temp.sort(reverse=True)
# print(temp)
for i in range( 1, n+1 ):
    temp[i-1] = temp[i-1] + i

print(max(temp) + 1)