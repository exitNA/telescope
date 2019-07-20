import pandas as pd

from opt.numerical_property import NumericalProperty


def test_numerical_property():
  opt = NumericalProperty()

  df = pd.DataFrame({
    'x': [1, 1]
  })
  ret = opt(df.x)
  assert 1 == ret['mean']
  assert 0 == ret['std']
  assert 1 == ret['median']

  df = pd.DataFrame({
    'x': [1, 2, 3]
  })
  ret = opt(df.x)
  assert 2 == ret['mean']
  assert 1 == ret['std']
  assert 2 == ret['median']
