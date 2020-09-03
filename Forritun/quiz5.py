#max_int = 0
#while True:
#    num_int = int(input("Input a number: "))
#    if num_int < 0:
#        break
#    max_int = max(num_int,max_int)
#
#print("The maximum is", max_int)


n = int(input("Enter the length of the sequence: "))

i = 0
summa = 0
tala1 = 0
tala2 = 0
tala3 = 0

for i in range(1 , n+1):
    if i == 1:
        tala1 = i
        print(tala1)
    elif i == 2:
        tala2 = i
        print(tala2)
    elif i == 3:
        tala3 = i
        print(tala3)
    else:
        summa = tala1 + tala2 + tala3
        tala1 = tala2
        tala2 = tala3
        tala3 = summa
        print(summa)

