
O = ["a","b","c","d","e","f","g","h","i","j","k",
        "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

I = [-1] * 26

strlist = list(input())

for i in range(len(O)):
        try:
                tempInx = strlist.index(O[i])
        except:
                tempInx = -1

        I[i] = tempInx

for element in I:
    print(element , end = " ")