import numpy as np

from papatya import data as d
from papatya import errors

def test_to_onehot():
    a = ['a', 'a', 'b', 'a', 'c']
    a = d.to_onehot(a)
    b = np.asarray([[1,0,0],[1,0,0],[0,1,0],[1,0,0],[0,0,1]])
    for i in range(5):
        for j in range(3):
            assert a[i][j] == b[i][j]
    c = "string type"
    try:
        d.to_onehot(c)
        assert False
    except errors.UnknownTypeError:
        assert True

def test_normalize():
    a = [0, 5, 3, 6, 10]
    a = d.normalize(a)
    b = np.asarray([0.0, 0.5, 0.3, 0.6, 1])
    for i in range(5):
        assert a[i] == b[i]
    c = "string type"
    try:
        c = d.normalize(c)
        assert False
    except:
        assert True

def test_concatenate():
    a = np.asarray([[1,2,3],[4,5,6]])
    b = np.asarray([1,2])
    c = d.concatenate([a,b])
    for i in range(2):
        assert c.shape[0] == 2
        assert c.shape[1] == 4
    e = np.asarray([[1,2,3],[4,5,6],[7,8,9]])
    try:
        c = d.concatenate([a,b,e])
        assert False
    except errors.InvalidShape:
        assert True
    e = np.asarray([[[1,2],[2,3]],[[3,4],[4,5]]])
    try:
        c = d.concatenate([a,b,e])
        assert False
    except errors.InvalidShape:
        assert True
