import numpy as np

from opt.base_operator import BaseOperator


class NumericalProperty(BaseOperator):
  def __call__(self, series, *args, **kwargs):
    mean = np.mean(series)
    std = np.std(series)
    median = np.median(series)
    return {
      'mean': mean,
      'std': std,
      'median': median
    }
