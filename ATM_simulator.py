message = """Please choose your option   
1--> Check balance
2--> Deposit Amount
3--> Withdrawl """
print(message)
task = int(input("Enter your option : "))
available_amount = 5000
if (task >= 1) and (task <= 3):
    if task == 1:
        # balance
        check_message = f"Your availabe balance is {available_amount}"
        print(check_message)
    elif task == 2:
        # deposit
        deposit_amount = int(input("Please enter your deposit amount : "))
        if deposit_amount > 0:
            available_amount += deposit_amount
            print("Your amount is successfully deposited.")
            check_message = f"Your availabe balance is {available_amount}"
            print(check_message)
        else:
            print("Please enter a valid deposit amount.")
    else:
        withdrawl_amount = int(input('Please enter your withdrawl amount :'))
        if (withdrawl_amount > 0) and (withdrawl_amount <= available_amount):
            available_amount -= withdrawl_amount
            print("Your amount is successfully extracted.")
            check_message = f"Your availabe balance is {available_amount}"
            print(check_message)
        else:
            print("Please enter a valid withdrawl amount.")
else:
    print("Please choose correct option.")
