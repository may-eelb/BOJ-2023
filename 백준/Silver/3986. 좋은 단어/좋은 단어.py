from sys import stdin
input = stdin.readline

n = int(input())


count = 0

for i in range(n):
    stack = []
    temp = list(input().strip())

    for c in temp:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    if not stack:
        count += 1

print(count)

