import re

a = "255.127.88.3"
b = "255a.127.88.3"
c = "127.0.0.257"

y = "regexp"

def is_ip(x):
    try:
        x = x.split('.')
        valid = [int(b) for b in x]
        valid = [b for b in valid if b >= 0 and b <= 255]
        return len(x) == 4 and len(valid) == 4
    except:
        return False

print(is_ip(a))
print(is_ip(b))
print(is_ip(c))