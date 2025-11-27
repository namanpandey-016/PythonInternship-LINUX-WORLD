#ATM PIN SYSTEM

balance = 5000
pin = 1234
attempts = 0
while attempts < 3:
    userpin = int(input("Enter userpin: "))
    if userpin == pin :
        amount = int(input("Enter amount: "))
        if amount <= balance :
            balance -= amount
            print("withdrawl is successful")
            print("remainiing balance : ", balance)
        else :
            print("Insufficient balance")
    else :
        attempts += 1 
        print("Pin is wrong")
    if attempts == 3:
        print("Your ATM is deactivated")
