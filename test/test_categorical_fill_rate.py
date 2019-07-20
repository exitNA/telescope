import pandas as pd

from opt.fill_rate import CategoricalFillRate


def test_categorical_fill_rate():
    opt = CategoricalFillRate()
    df = pd.DataFrame({
        'x': ['1']
    })
    ret = opt(df.x)
    assert 1 == ret['quantity']
    assert 1 == ret['fill_rate']

    df = pd.DataFrame({
        'x': ['a']
    })
    ret = opt(df.x)
    assert 1 == ret['quantity']
    assert 1 == ret['fill_rate']

    df = pd.DataFrame({
        'x': ['a', '1']
    })
    ret = opt(df.x)
    assert 2 == ret['quantity']
    assert 1 == ret['fill_rate']


def test_categorical_fill_rate_with_empty_string():
    opt = CategoricalFillRate()
    df = pd.DataFrame({
        'x': ['']
    })
    ret = opt(df.x)
    assert 0 == ret['quantity']
    assert 0 == ret['fill_rate']

    df = pd.DataFrame({
        'x': ['a', '']
    })
    ret = opt(df.x)
    assert 1 == ret['quantity']
    assert 0.5 == ret['fill_rate']


def test_categorical_fill_rate_with_none():
    opt = CategoricalFillRate()
    df = pd.DataFrame({
        'x': [None]
    })
    ret = opt(df.x)
    assert 0 == ret['quantity']
    assert 0 == ret['fill_rate']

    df = pd.DataFrame({
        'x': ['a', None]
    })
    ret = opt(df.x)
    assert 1 == ret['quantity']
    assert 0.5 == ret['fill_rate']