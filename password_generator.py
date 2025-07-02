import random
import string

def generate_password():
    length = random.randint(8, 16)

    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining = random.choices(all_chars, k=length - 4)

    password_list = list(upper + lower + digit + symbol + ''.join(remaining))
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password



print("Your Strong Password:", generate_password())
