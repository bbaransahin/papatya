import numpy as np

from papatya import analyze as an

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
