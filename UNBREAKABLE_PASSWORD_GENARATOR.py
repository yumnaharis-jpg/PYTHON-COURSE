import random
import string
def generate_password(Length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(Length))
    return password
Length = int(input("Enter the length of the password: "))
print("Generated password: " + generate_password(Length))
5














