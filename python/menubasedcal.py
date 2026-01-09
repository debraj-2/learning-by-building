name = input("Enter your name:")
age = int(input("Enter your age:"))
current_year = 2026

print("----USER LIFE REPORT----")
print("\n Choose an option")
print("1. Show birth year")
print("2. Age after 10 years")
print("3. Voting status")
print("4. How many days lived")
print("5. Exit")

choice = input("Enter your desired choice")

if choice == "1":
    print("Birth year:", current_year - age)
elif choice == "2":
    print("Age after 10 years:", age + 10)
elif choice == "3":
    if age >= 18:
        print("Eligible for Vote") 
    else:
        print("Not Eligible for Vote")    
elif choice == "4":
    print("Days lived approximately:", age * 365)
elif choice == "5":
    print("Goodbye!", name)
else :
    print("Invalid Choice , go and try again")                       