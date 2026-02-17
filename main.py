import string
import random

# Define Functions
def passwordGen():
    # Define Lists to get password from
    charsWithoutExtras = string.ascii_letters + string.digits
    charsWithExtras = charsWithoutExtras + "-" + "!"

    # Get Users Options for Password
    print("Welcome to Password Gen!")
    length = int(input("Password Length: "))
    extras = input("Do you want -'s and !'s? (y/n): ")
    
    # Genarate
    if extras == "y":        
        for x in range(0, length):
            randomchar = random.choice(charsWithExtras)
            print(randomchar, end='')
        print("\n")
    elif extras == "n":
        for x in range(0, length):
            randomchar = random.choice(charsWithoutExtras)
            print(randomchar, end='')
        print("\n")

def greet():
    # Get name annd print using f string to insert varibles
    name = input("What's your name?: ")
    print(f"Hello, {name.title()}!")

# Get User Choice
print("""
    1. Password Gen
    2. Greeting Machine
""")

choice = input("Choose One: ")
if choice == "1":
    passwordGen()
elif choice == "2":
    greet()
elif choice == "q":
    exit()