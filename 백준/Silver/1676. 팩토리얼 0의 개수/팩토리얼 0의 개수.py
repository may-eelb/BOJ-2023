from collections import deque

N = int(input())
p = 0
for i in range (N+1):
    if (i == 1):
        p +=1
    elif ( i >1) :
        p *= i

#print(p)

my_deque = deque(list(digit for digit in str(p)))

#print(my_deque)
my_deque.reverse()
#print(my_deque)
count = 0

while (my_deque[0] == '0' ):
    if len(my_deque) == 1:
        break

    my_deque.rotate(-1)
    count += 1

print(count)