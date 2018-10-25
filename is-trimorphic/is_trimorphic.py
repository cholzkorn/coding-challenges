# Function to check if a number is trimorphic
# A trimorphic number is a number whose cube ends in itself
# Input 4: TRUE - (4^3 is 64, which ends in 4)
# Input 13: FALSE - (13^3 is 2197, which ends in 97)

import re

def is_trimorphic(x):
    xc = x ** 3
    xs = str(x)
    xcs = str(xc)
    pattern = re.escape(xs) + r"$"
    match = re.search(pattern, xcs)
    if match:
        return True
    else:
        return False
