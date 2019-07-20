import numpy as np
import pandas as pd

from diff import Diff

if __name__ == '__main__':
  df1 = pd.DataFrame({
    'x': [None, 2, np.NaN, 3, np.Inf],
    'y': ['', 2, np.NaN, None, '1']
  })

  df2 = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': ['a', 'b', 'c', 'd']
  })

  diff = Diff()
  diff(df1, df2)
