import numpy as np

tri1 = [3, 4, 5]
tri2 = [7, 9, 1]

# the sum of two sides always has to be greater than the 3rd side

def is_triangle(x):
  if x[0] + x[1] > x[2] and x[1] + x[2] > x[0] and x[0] + x[2] > x[1]:
    return(True)
  else:
    return(False)

print(is_triangle(tri1))
print(is_triangle(tri2))
