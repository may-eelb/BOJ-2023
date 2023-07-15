
A, B, V = map(int, input().split())

day = 0

x = V - A
day += 1

if x % ( A - B ) == 0:
    day += x // ( A - B)
else:
    day +=  ( x // (A - B) + 1 )


print(day)
