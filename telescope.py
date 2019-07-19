from fill_rate import FillRate
import numpy as np
import pandas as pd


if __name__ == '__main__':
    df = pd.DataFrame({
        'x': [None, 2, np.NaN, 3, np.Inf],
        'y': ['', 2, np.NaN, None, '1']
    })

    opt = FillRate()
    for c in df:
        print(c, type(df[c].iloc[2]))
        print(df[c])
        print(opt(df[c]))