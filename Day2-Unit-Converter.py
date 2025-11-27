# Day-2-Calculator-For-MeasurementChanges
#A simple program that will change the input form one unit to another unit
while True:
    print("""
    1: cm to m
    2: m to cm
    3: inch to cm
    4: m to km
    5: Exit""")

    choice = input("Enter your choice: ")

    if choice == "1":
        num1 = float(input("Enter Value: "))
        print("In M:", num1 / 100)

    elif choice == "2":
        num1 = int(input("Enter Value: "))
        print("Subtraction is:", num1 * 100)

    elif choice == "3":
        num1 = int(input("Enter number 1: "))
        print("Multiplication is:", num1 * 2.54)

    elif choice == "4":
        num1 = int(input("Enter number 1: "))
        print("Multiplication is:", num1 * 1000)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
