import numpy as np


class BaseOperator:
    pass


class NumericalFillRate(BaseOperator):
    def __init__(self):
        self._empty_set = {None, '', np.NaN}

    def __call__(self, series, *args, **kwargs):
        def _is_empty(x):
            return x in self._empty_set

        total = series.shape[0]
        # empty_num = series.apply(_is_empty).sum()
        empty_num = np.isnan(series).sum()
        not_empty_num = total - empty_num

        return {
            f'{series.name}-empty': empty_num,
            f'{series.name}-fill_rate': not_empty_num / total
        }


class CategoricalFillRate(BaseOperator):
    def __init__(self):
        self._empty_set = {None, '', np.NaN}

    def __call__(self, series, *args, **kwargs):
        def _is_empty(x):
            return x in self._empty_set

        total = series.shape[0]
        # empty_num = series.apply(_is_empty).sum()
        empty_num = np.isnan(series).sum()
        not_empty_num = total - empty_num

        return {
            f'{series.name}-empty': empty_num,
            f'{series.name}-fill_rate': not_empty_num / total
        }
