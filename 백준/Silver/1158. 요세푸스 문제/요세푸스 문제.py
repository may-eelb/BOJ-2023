from collections import deque

N, K = map(int, input().split())

my_list =[]
for i in range(1, N+ 1):
    my_list.append(i)

my_deque = deque(my_list)
answer = []
while my_deque:
    my_deque.rotate(-K+1)
    answer.append(my_deque.popleft())

print("<", end ="")

for i in range(len(answer) - 1):
    print(f'{answer[i]}, ', end ="")


print(f'{answer[-1]}>')
