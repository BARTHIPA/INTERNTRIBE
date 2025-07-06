def get_password_length(min_length=6):
    while True:
        try:
            length = int(input("Enter desired password length: "))
            if length < min_length:
                print(f"Password length must be at least {min_length}. Please try again.")
            elif length <= 0:
                print("Password length must be a positive number. Please try again.")
            else:
                print(f"Password length accepted: {length}")
                return length
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

password_length = get_password_length()
