while(1):
    choice = input("Enter operation : ")
    if (choice == '+'):
        print("Sum = ",int(input("Enter 1st Number : "))+int(input("Enter 2nd number : ")))
    elif(choice == '-'):
        print("Difference = ",int(input("Enter 1st Number : "))-int(input("Enter 2nd number : ")))
    elif(choice == '*'):
        print("multiply = ",int(input("Enter 1st Number : "))*int(input("Enter 2nd number : ")))
    elif(choice == '/'):
        print("divide = ",int(input("Enter 1st Number : "))/int(input("Enter 2nd number : ")))
    elif(choice == 'rem'):
        print("remainder = ",int(input("Enter 1st Number : "))%int(input("Enter 2nd number : ")))
    else:
        break