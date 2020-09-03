print("Welcome to car rentals!")
cont = input("Would you like to continue (y/n)? ") 
while cont == "y" : # Forritið á að keyrast meðan cont = strengurinn y
    code = input("Customer code (b or d): ")
    days = int(input("Number of days: "))
    odo_start = int(input("Odometer reading at the start: "))
    odo_end = int(input("Odometer reading at the end: "))
    odo_tot = odo_end - odo_start
    print("Miles driven:",odo_tot)
    if code == "b" : # ef notandi slær b notast við þessa
        amount = float((40 * days)+(0.25 * odo_tot)) # reikna lokaupphæðina með float fallinu
    elif code == "d": # ef notandi slær inn d notast við þessa
        odo_d = odo_tot - (days * 100) # odo_d er mílur umfram 100 mílur á dag
        amount = float((60 * days)+(0.25 * odo_d ))
    amount_fin = round(amount , 1) # Námunda að einum aukastaf með round falli
    print("Amount due:",amount_fin) 
    cont = input("Would you like to continue (y/n)? ") # set aftur aftast til að vera með það í lykkjuni


