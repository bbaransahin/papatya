import numpy as np

from papatya import data as d

def test_to_onehot():
    a = ['a', 'a', 'b', 'a', 'c']
    a = d.to_onehot(a)
    b = np.asarray([[1,0,0],[1,0,0],[0,1,0],[1,0,0],[0,0,1]])
    for i in range(5):
        for j in range(3):
            assert a[i][j] == b[i][j]

def test_normalize():
    a = [0, 5, 3, 6, 10]
    a = d.normalize(a)
    b = np.asarray([0.0, 0.5, 0.3, 0.6, 1])
    for i in range(5):
        assert a[i] == b[i]
