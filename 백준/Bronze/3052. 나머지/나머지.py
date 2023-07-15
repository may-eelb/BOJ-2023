

mylist = []
for _ in range(10):
        num = int(input())
        나머지 = num % 42
        mylist.append(나머지)

print(len(list(set(mylist))))


