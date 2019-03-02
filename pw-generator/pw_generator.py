import random as rd
import string

def generate_password(x):
    random = ''.join([rd.choice(string.ascii_letters + string.digits)
    for n in range(x)])
    print(random)
    return random

generate_password(12)