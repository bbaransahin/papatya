import numpy as np
import pandas as pd

from papatya import analyze as an
from papatya import errors

def test_nanstat_ndarray():
    # 1-D test
    a = np.asarray([np.NaN, 1, 3, 5, 3, np.NaN])
    res = an.nanstat_ndarray(a)
    assert res[0] == 2
    assert res[1] == 6
    # 2-D test
    a = np.asarray([
        [np.NaN, np.NaN, np.NaN, np.NaN],
        [1, 2, 4, 1],
        [np.NaN, 3, 5, np.NaN]
        ])
    res = an.nanstat_ndarray(a)
    assert res[0] == 6
    assert res[1] == 12
    assert res[2] == 2
    assert res[3] == 1
    assert res[4] == 1
    assert res[5] == 2
    a = np.asarray([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
        ])
    try:
        res = an.nanstat_ndarray(a)
        assert False
    except errors.InvalidShape:
        assert True

def test_get_max_min():
    # 1-D test
    a = np.asarray([1,2,3,4,5])
    min_val, max_val = an.get_max_min(a)
    assert min_val == 1
    assert max_val == 5
    a = pd.Series(a)
    min_val, max_val = an.get_max_min(a)
    assert min_val == 1
    assert max_val == 5
    # 2-D test
    a = np.asarray([
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ])
    min_val, max_val = an.get_max_min(a)
    assert min_val == 1
    assert max_val == 9
    a = pd.DataFrame(a)
    min_val, max_val = an.get_max_min(a)
    assert min_val == 1
    assert max_val == 9
    # Unkown shape
    a= np.asarray([
        [[1,0],[2,0],[3,0]],
        [[4,0],[5,0],[6,0]]
        ])
    try:
        min_val, max_val = an.get_max_min(a)
        assert False
    except errors.UnknownTypeError:
        assert True
