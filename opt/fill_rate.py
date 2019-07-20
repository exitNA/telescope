import numpy as np

from opt.base_operator import BaseOperator


class FillRate(BaseOperator):
  def is_empty(self, x):
    raise NotImplementedError()

  def __call__(self, series, *args, **kwargs):
    total = series.shape[0]
    quantity = total - series.apply(self.is_empty).sum()
    return {
      'quantity': quantity,
      'fill_rate': quantity / total
    }


class NumericalFillRate(FillRate):
  def is_empty(self, x):
    return x is None or np.isnan(x)


class CategoricalFillRate(FillRate):
  def __init__(self):
    self._empty_set = {None, ''}

  def is_empty(self, x):
    return x in self._empty_set


class MultiValueFillRate(FillRate):
  def is_empty(self, x):
    return x is None or len(x) == 0
