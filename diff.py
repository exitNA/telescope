from loguru import logger
import numpy as np
from opt.fill_rate import *


def get_column_dtype(series):
  first_val = series.iloc[0]
  return type(first_val)


def _get_fill_rate(dtype, series):
  if CategoricalFillRate.is_dtype_supported(dtype):
    opt = CategoricalFillRate()
  elif NumericalFillRate.is_dtype_supported(dtype):
    opt = NumericalFillRate()
  elif MultiValueFillRate.is_dtype_supported(dtype):
    opt = MultiValueFillRate()
  else:
    raise NotImplementedError(f'{dtype} not supported for fill rate calculate')

  return opt(series), opt.__class__.__name__


class Diff:
  def __init__(self):
    self._detail = []

  def __call__(self, *args, **kwargs):
    logger.debug('analysis each df')
    for df in args:
      detail = self.analysis_data_frame(df)
      logger.info('detail {}', detail)

  def analysis_data_frame(self, df):
    row_num = df.shape[0]
    column_info = {}

    for col in df.columns:
      dtype = get_column_dtype(df[col])
      column_info[col] = {
        'dtype': dtype.__name__
      }
      ret, opt_name = _get_fill_rate(dtype, df[col])
      column_info[col][opt_name] = ret

    self._detail.append(column_info)
    return column_info
