
A = int(input())

for i in range( A // 5 , -1, -1):
    total = -1
    big = i

    temp = A - ( 5 * i )

    if (temp % 3 == 0):
        total = 0
        total += big
        small = temp // 3
        total+= small
        break;

print(total)