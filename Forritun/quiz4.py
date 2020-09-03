#highest = int(input("Input an int: "))
#for i in range(1, highest+1 ):
#    if i % 3 == 0:
#        print(i)

#first = int(input("Input the first integer: "))
#second = int(input("Input the second integer: "))
#sum = 0
#for i in range(1 , first+1 ):
#    sum = sum  + second
#print(sum)


#max_days = int(input("Input max number of days: "))
#target = int(input("Input dollar target: "))
#sum = 0
#for i in range(1 , max_days):
#    sum = 2 ** i
#    if sum >= target:
#        days_when_amount_acquired = i
#        print('Days needed:',days_when_amount_acquired)
#        break
#else:
#    days_when_amount_acquired = 0
#    print('Days needed:',days_when_amount_acquired)

#num = int(input("Input an int: "))
#sum = 0
#for i in range(1 , num + 1):
#    sum = sum + i
#    print(sum)

length = int(input("Input the length of series: "))
sum = 0
for i in range(1 , length + 1):
    if i % 2 == 0:
        sum_1 = -(i * 2)
    else:
        sum_1 = i * 2
    print(sum_1)
    sum = sum + sum_1
print("Sum:",sum)
