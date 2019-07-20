from loguru import logger
from opt.fill_rate import *
from opt.numerical_property import *


def get_column_dtype(series):
    first_val = series.iloc[0]
    return type(first_val)


def _get_fill_rate(dtype, series):
    opt = {
        str: CategoricalFillRate(),
        int: NumericalFillRate(),
        float: NumericalFillRate()
    }
    return opt[dtype](series)


class Diff:
    def __init__(self):
        self._report = []

    def __call__(self, *args, **kwargs):
        logger.debug('analysis each df')
        for df in args:
            report = self.analysis_data_frame(df)
            logger.info('report {}', report)

    def analysis_data_frame(self, df):
        row_num = df.shape[0]
        column_info = {}

        for col in df.columns:
            dtype = get_column_dtype(df[col])
            column_info[col] = {
                'dtype': dtype
            }
            ret = _get_fill_rate(dtype, df[col])
            column_info[col].update(ret)

        self._report.append(column_info)
        return column_info
