import random
import string

def display_intro():
    print("========================================")
    print("        PYTHON PASSWORD GENERATOR       ")
    print("========================================")
    print("This program generates a strong and secure password")
    print("based on the length and complexity selected by the user.\n")

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 4:
                print("Password length must be at least 4. Try again.")
            else:
                return length
        except ValueError:
            print("Invalid input! Please enter a number.")

def choose_complexity():
    print("\nChoose the password complexity level:")
    print("1. Only Letters (A-Z, a-z)")
    print("2. Letters + Numbers")
    print("3. Letters + Numbers + Special Characters")
    
    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

def generate_password(length, complexity):
    if complexity == "1":
        characters = string.ascii_letters
    elif complexity == "2":
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

def main():
    display_intro()
    
    length = get_password_length()
    complexity = choose_complexity()

    print("\nGenerating password... Please wait...\n")
    password = generate_password(length, complexity)

    print("========================================")
    print("              PASSWORD READY            ")
    print("========================================")
    print("Generated Password:", password)
    print("========================================")

# Run the program
main()
