# STORED CREDENTIALS

saved_username = "Debraj"
balance = 20000000000.00
saved_pin = 1234
attempts = 4

# LOGIN SYSTEM

while attempts > 0:
    username = input("Enter username: ")
    pin = int(input("Enter PIN: "))
    if username == saved_username and pin == saved_pin:
        print(f"\n ✔️ Login Successful! welcome {username}")
        break
    else:
        attempts -= 1
        print(f"\n ❌ Login Failed ! Invalid credentials. You have {attempts} attempts left.")
if attempts == 0:
    print("\n ❌ Account Locked! Too many failed attempts Try Later.") 
else:
    
    #ATM MENU
    print("\n ----ATM MENU----")
    print("1. Check Balance")
    print("2. Deposit") 
    print("3. Withdraw") 
    print("4. Exit")
    
    choice = int(input("Enter your choice:"))
    
    if choice == 1:
        print(f"\n Your current balance is : ₹{balance}")
    
    elif choice == 2:
        amount = float(input("Enter amount to deposit"))
        balance += amount
        print(f"\n ✅ {amount} has been deposited successfully.")
        print(f"\n Updated balance: ₹{balance}")
         
    elif choice == 3:
        amount = float(input("Enter amount to withdraw:"))
        if amount <= balance:
            balance -= amount
            print(f"\n ✅ Please collect your cash.")
            print(f"\n Remaining Balance: ₹{balance}")
        else:
            print("\n ❎ insufficient balance!")
    
    elif choice == 4:
        print("\n Thank you for using our ATM Service , have a great day ahead! 🙏  ")
        
    
    else:
        print("\n❌ invalid choice , please try again.")                        