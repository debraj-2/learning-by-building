name = input("Enter your name:")
balance = float(input("Enter your current balance:"))

print("\n----ATM MENU----")
print("1. Deposit")
print("2. Withdraw")

choice = int(input("Enter your choice (1 or 2):"))

if choice == 1:
    amount = float(input("Enter amount to deposit:"))
    balance = balance + amount
    print(f"\n{name}, your money has been deposited successfully.")
    print(f"Updated balance: ₹{balance}")
    
elif choice == 2:
    amount = float(input("Enter amount to withdraw:"))
    if amount <= balance:
        balance = balance - amount
        print(f"\n{name}, please collect your cash.")
        print(f"Remaining balance: ₹{balance}")
    else:
        print("\n ❌Insufficient balance!")
        
else:
    print("\n❌ Invalid choice , please try again.") 
    
print("\n Thank you for using our ATM service , have a great day ahead!🙏")                   
    