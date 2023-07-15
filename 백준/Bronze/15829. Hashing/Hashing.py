N = int(input())
mystr = input()


sum = 0
for i in range(N):
    temp = ord(mystr[i]) - 96
    sum = sum + temp * ( 31 ** i)

print( sum % 1234567891 )