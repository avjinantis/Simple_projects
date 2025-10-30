import random
import getpass
import string

def password_checker(password):
    deffects = []
    if len(password) < 8:
        deffects.append("Atleast 8 characters.")
    if not any(char.islower() for char in password):
        deffects.append("Missing lower case letter.")
    if not any(char.isupper() for char in password):
        deffects.append("Missing upper case letter.")
    if not any(char.isdigit() for char in password):
        deffects.append("Missing digits.")
    if not any(char in string.punctuation for char in password):
        deffects.append("Missing punctuation.")

    return deffects

def password_suggestion():
    full_str = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(full_str) for _ in range(7))
while True:
    password = getpass.getpass("Enter your password: ")
    issues = password_checker(password)
    if not issues:
        print("Password confirmed.")
        exit(0)
    else:
        print("Password not satisfactory")
        print("Issues are: ")
        for item in issues:
            print(item)
        choice = input("Do you want suggestion for the password (y/n): ").lower()
        if choice == 'y':
            while True:
                sug_pass = password_suggestion()
                print("Suggested password: ",sug_pass)
                ch = input("Confirm the password (y/n)\nenter -1 to exit from password suggestions.\nEnter your choice: ").lower()
                if ch == 'y':
                    print("Password confirmed.")
                    exit(0)
                elif ch=='-1':
                    break
                elif ch=="n":
                    continue
                else:
                    print("Invalid option! Try again.")
                    break
        elif choice == 'n':
            continue
        else:
            print("Invalid option! Try again")
            continue