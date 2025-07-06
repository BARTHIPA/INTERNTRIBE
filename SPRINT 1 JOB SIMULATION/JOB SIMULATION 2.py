import random
import string

def generate_password(length):
    if length < 2:
        return "Password length must be at least 2 to include a letter and a number."

    password = []
    
    
    password.append(random.choice(string.ascii_letters))             
    for _ in range(length - 2):
        char_type = random.choice(['letter', 'digit', 'symbol'])
        if char_type == 'letter':
            password.append(random.choice(string.ascii_letters))
        elif char_type == 'digit':
            password.append(random.choice(string.digits))
        else:
            password.append(random.choice(string.punctuation))

   
    random.shuffle(password)

    
    return ''.join(password)


length = 8 
final_password = generate_password(length)
print("Generated Password:", final_password)
