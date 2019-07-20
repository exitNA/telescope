import numpy as np
import pandas as pd

from opt.fill_rate import NumericalFillRate


def test_numerical_fill_rate():
  df = pd.DataFrame({
    'x': [1]
  })

  opt = NumericalFillRate()
  ret = opt(df.x)
  assert 1 == ret['quantity']
  assert 1.0 == ret['fill_rate']


def test_numerical_fill_rate_with_nan():
  df = pd.DataFrame({
    'x': [1, np.NaN]
  })
  opt = NumericalFillRate()
  ret = opt(df.x)
  assert 1 == ret['quantity']
  assert 0.5 == ret['fill_rate']


def test_numerical_fill_rate_with_none():
  df = pd.DataFrame({
    'x': [None, 1]
  })
  opt = NumericalFillRate()
  ret = opt(df.x)
  assert 1 == ret['quantity']
  assert 0.5 == ret['fill_rate']
