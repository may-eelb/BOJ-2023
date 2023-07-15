n = int(input())

for _ in range(n):
    count, word = input().split()
    for x in word:
        print(x * int(count), end = '')
    print()