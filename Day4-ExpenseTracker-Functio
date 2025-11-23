# Day-4-Project-Expense-Tracker
mylist = []
def add():
    b = int(input("enter your Expense you want to add"))
    mylist.append(b)
    print("Your expense is recorded")

def remov():
    rmv = float(input("Enter the value you want to remove: "))
    if rmv in mylist:
        mylist.remove(rmv)
        print("Your entered Expense is removed")
    else :
        print("Your entered Expense is not in list")

def exp():
    print("Your expenses are: ")
    print(mylist)

def total():
    total_sum = sum(mylist)
    print(f"The sum of the Expenses is: {total_sum}")
    
print("Wanna Track you expenses")
while True:
    print("""
    1: Add Expense
    2: Remove
    3: Display
    4: Total
    5: Exit""")
    

    choice = input("Enter your choice: ")
    
    if choice == "1":
        add()
        
    elif choice == "2":
        remov()
        
    elif choice == "3":
        exp()
        
    elif choice == "4":
        total()
        
    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")


