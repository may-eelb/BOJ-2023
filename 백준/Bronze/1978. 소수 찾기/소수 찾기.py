
N = int(input())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

cnt = 0
numbers = list(map(int, input().split()))

for i in range(N):
    if (is_prime(numbers[i])):
        cnt +=1

print(cnt)