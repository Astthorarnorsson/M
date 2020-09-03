#num = int(input("Input an int: "))
#counter = 0

#while counter < num:
#    print(num)
#    num -= 1

#num = int(input("Input an int: "))
#counter = 0

#while counter < num:
#    counter += 1
#    print(counter*2)

#num = int(input("Input an int: "))
#counter = num
#sum = 0

#while num != 10:
#    sum += num # sum = sum + num
#    num = int(input("Input an int: "))

#print(sum)

#n = int(input("Input an int: "))
#counter = 1

#while counter <= n:
#    if n % counter == 0:
#        print(counter)
#    counter += 1

rating = int(input("Input elo rating: ")) 

while rating > 1:
    if rating >= 2700:
        print("Super grandmaster")
    elif 2700 > rating >= 2500:
        print("Grandmaster")
    elif 2500 > rating >= 2400:
        print("International")
    elif 2400 > rating >= 1000:
        print("Amateur")
    elif 1000 > rating > 1:
        print("Invalid")
    rating = int(input("Input elo rating: "))