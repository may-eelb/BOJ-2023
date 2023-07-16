from collections import deque

my_deque = deque()

N, M = map(int, input().split())

for i in range(1, N+1):
    my_deque.append(i)

result = []
my_deque.rotate( - (M-1))
while my_deque:
    result.append(my_deque.popleft())
    my_deque.rotate(- (M - 1))

print("<", end ="")
for j in range(len(result)-1):
    print( result[j], end =", ")
print(f'{result[-1]}>')
