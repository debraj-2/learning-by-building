name = input("Enter your Name:")
age = int(input("Enter your Age: "))
current_year = 2026

birth_year = current_year - age
future_age = age + 10
year_100 = current_year + (100 - age)

print("\n----USER LIFE REPORT----")
print(f"\nHello {name}")
print(f"You were born in {birth_year}")
print(f"In 10 years, you will be {future_age}")
print(f"You will turn 100 in the year {year_100}")

if age>= 18:
    print("Voting Status : Eligible for Vote ")
else:
    print("Voting Status : Not Eligble for Vote ")
    
print(f"You have lived approximstely {age * 365} days")        