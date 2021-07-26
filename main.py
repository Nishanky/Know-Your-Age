thisyear = 2021

name = input("Hey there! Please Enter your name..")

if name.isnumeric():
    print("You entered some numbers instead of your name!!")
    exit()

age = 0

try:
    age = int(input(f"Hello {name}:)\nEnter your age or year of birth:"))
except ValueError:
    print("Enter a numeric value..")
    exit()

birth_year = age


if len(str(age)) <= 3:
    print("You Entered your age..")
    birth_year = thisyear - age
    print("Your birth year is:", birth_year)

if birth_year > thisyear:
    print("You are not yet born..")
    exit()

if thisyear - birth_year > 150:
    print("You are oldest person alive!!")

choice = int(input("What you want to know??\n"
      "1. When you will turn 100 years old\n"
      "2. Your current age\n"
      "3. Your age in any particular year"))

if choice == 1:
    print("You will turn 100 years old in:", birth_year + 100)

elif choice == 2:
    print("Your current age is:", thisyear - birth_year)

elif choice == 3:
    year = int(input("Enter the year in which you want to know your age.."))
    if year < birth_year:
        raise Exception(f"Your were not born in {year}")
    print(f"Your age in {year} will be {year - birth_year}")

else:
    print("You selected wrong option")



