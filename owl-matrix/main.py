# CODE CHALLENGE OWL MATRIX BY IDO SABAN ON SOLOLEARN
# www.github.com/cholzkorn

import pandas as pd
import numpy as np

# Creating sample matrix

X = {'col0': ["a", "c", "c", "a"],
     'col1': ["b", "c", "c", "b"],
     'col2': ["b", "c", "c", "b"],
     'col3': ["a", "c", "c", "a"]}

df = pd.DataFrame(data=X)

# Thoughts: Column i and n-i must always be the same
# Row m and m-i must always be the same
# Owl matrices must be square, therefore n = m = len(matrix)

# Writing the function

def owl_matrix(df):
    # Columns (n)
    ixn = 0
    nb = [0] * len(df) # List of boolean values
    for i in df:
        nb[ixn] = np.array(df.iloc[ixn, :].all() == np.array(df.iloc[len(df)-1-ixn, :].all()))
        ixn += 1
    ntr = sum(nb) == len(df)

    # Rows (m)
    ixm = 0
    mb = [0] * len(df) # List of boolean values
    for i in df:
        mb[ixm] = np.array(df.iloc[:, ixm].all() == np.array(df.iloc[:, len(df) - 1 - ixm].all()))
        ixm += 1
    mtr = sum(mb) == len(df)

    # Final comparison and returning boolean
    print(ntr and mtr)
    if ntr and mtr:
        return True
    else:
        return False

# Calling the function

owl_matrix(df)