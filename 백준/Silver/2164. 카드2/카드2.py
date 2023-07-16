
from collections import deque


N = int(input())
my_deque = deque(list(range(1, N+1)))


while(len(my_deque) != 1):
    my_deque.popleft()
    my_deque.rotate(-1)


print(my_deque.pop())