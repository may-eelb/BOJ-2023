N = int(input())

for _ in range(N):
        sumO = 0
        temp = 0

        mystr = list(input())
        for i in range(len(mystr)):

                if mystr[i] == 'O' :
                        temp = temp + 1
                        sumO = sumO + temp
                else:
                        temp = 0

        print(sumO)

