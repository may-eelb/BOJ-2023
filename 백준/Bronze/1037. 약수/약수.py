from sys import stdin
input = stdin.readline

N = int(input())
ml = list(map(int, input().split()))

temp = sorted(ml)
print(temp[0] * temp[-1])