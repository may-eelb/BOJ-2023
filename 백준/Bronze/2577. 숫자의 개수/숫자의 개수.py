

A = int(input())
B = int(input())
C = int(input())

곱 = A * B * C
곱_list = list(str(곱))

for i in range(10):
    temp = 곱_list.count(str(i))

    print(temp)
