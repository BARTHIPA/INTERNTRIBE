import random
import string


while True:
    try:
        length = int(input("Enter password length (minimum 6): "))
        if length < 6:
            print("Password must be at least 6 characters.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")


password = []


password.append(random.choice(string.ascii_letters))
password.append(random.choice(string.digits))


for _ in range(length - 2):
    password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))


random.shuffle(password)
print("Generated password:", ''.join(password))
