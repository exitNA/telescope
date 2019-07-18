from operator import *
import numpy as np
import pandas as pd


if __name__ == '__main__':
    df = pd.DataFrame({
        'x': [1, 2, np.NaN, 3, np.Inf],
        'y': ['', 'a', 'b', None, '1']
    })

    opt = FillRate()
    for c in df:
        print(opt(df[c]))