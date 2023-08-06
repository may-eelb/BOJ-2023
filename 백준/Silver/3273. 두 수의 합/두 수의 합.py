from sys import stdin
input = stdin.readline
import math

count = 0
n = int(input())
temp = list(map( int, input().split()))
target = int(input())

temp.sort()

start = 0
end = n-1
while start < end :
    if temp[start] + temp[end] < target:
        start+=1
    elif temp[start] + temp[end] > target:
        end -= 1
    else:
        count+=1
        start+=1
        end -=1

print(count)
