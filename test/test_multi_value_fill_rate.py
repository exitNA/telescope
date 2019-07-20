import pandas as pd

from opt.fill_rate import MultiValueFillRate


def test_multi_value_fill_rate():
  opt = MultiValueFillRate()
  df = pd.DataFrame({
    'x': [[1, 2]]
  })
  ret = opt(df.x)
  assert 1 == ret['quantity']
  assert 1 == ret['fill_rate']

  df = pd.DataFrame({
    'x': [[1], [2, 3]]
  })
  ret = opt(df.x)
  assert 2 == ret['quantity']
  assert 1 == ret['fill_rate']


def test_multi_value_fill_rate_with_none():
  opt = MultiValueFillRate()
  df = pd.DataFrame({
    'x': [None, [1, 2]]
  })
  ret = opt(df.x)
  assert 1 == ret['quantity']
  assert 0.5 == ret['fill_rate']


def test_multi_value_fill_rate_with_empty_list():
  opt = MultiValueFillRate()
  df = pd.DataFrame({
    'x': [[], [1, 2]]
  })
  ret = opt(df.x)
  assert 1 == ret['quantity']
  assert 0.5 == ret['fill_rate']
