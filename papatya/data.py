import numpy as np
import pandas as pd
from tqdm import tqdm

from papatya import errors

def to_onehot(s, verbose=True):
    '''
    This function transforms a data (ndarray, pandas.Series, etc.) to onehot format and returns.
    Implemented data types:
        numpy.ndarray
        pandas.core.series.Series
        list
    '''
    # Let's check if the given data shape is valid
    if (type(s) == np.ndarray and len(s.shape) == 1):
        pass
    elif (type(s) == pd.core.series.Series):
        pass
    elif (type(s) == list):
        pass
    else:
        raise errors.UnknownTypeError("Given data has unknown type. Given data type:"+str(type(s)))

    vals = []
    onehot = []

    #These blocks are both same, only difference is the tqdm.
    if (verbose):
        for v in tqdm(s):
            if (not v in vals):
                vals.append(v)
                for i in onehot:
                    i.append(0)
            onehot_item = []
            ind = vals.index(v)
            for i in range(len(vals)):
                if (i == ind):
                    onehot_item.append(1)
                else:
                    onehot_item.append(0)
            onehot.append(onehot_item)
    else:
        for v in s:
            if (not v in vals):
                vals.append(v)
                for i in onehot:
                    i.append(0)
            onehot_item = []
            ind = vals.index(v)
            for i in range(len(vals)):
                if (i == ind):
                    onehot_item.append(1)
                else:
                    onehot_item.append(0)
            onehot.append(onehot_item)

    onehot = np.asarray(onehot)
    return onehot

def normalize(s, verbose=True):
    '''
    This function normalizes a data between 0 and 1.
    '''
    # Let's check if the given data shape is valid
    if (type(s) == np.ndarray and len(s.shape) == 1):
        pass
    elif (type(s) == pd.core.series.Series):
        pass
    elif (type(s) == list):
        pass
    else:
        raise errors.UnknownTypeError("Given data has unknown type. Given data type:"+str(type(s)))

    normalized = []
    max_val = s[0]
    min_val = s[0]
    for v in s:
        if (v > max_val):
            max_val = v
        if (v < min_val):
            min_val = v
    if (verbose):
        for v in tqdm(s):
            normalized.append((v-min_val)/float(max_val-min_val))
    else:
        for v in s:
            normalized.append((v-min_val)/float(max_val-min_val))

    normalized = np.asarray(normalized)
    return normalized

def concatenate(ndarrays, verbose=True):
    '''
    This function concatenates ndarrays with same length and returns it.
    Example input ndarrays shape = [(500,4), (500,), (500,23)]
    '''
    # First let's check if the shape of ndarrays are proper to concatenate.
    for i in ndarrays:
        if(not i.shape[0] == ndarrays[0].shape[0]):
            raise errors.InvalidShape("Can't concatenate ndarrays with different lengths.")
    # Concatenation
    new_data = []
    for i in range(ndarrays[0].shape[0]):
        new_item = []
        for n in ndarrays:
            if(len(n.shape) == 1):
                new_item.append(n[i])
            elif(len(n.shape) == 2):
                for v in n[i]:
                    new_item.append(v)
            else:
                raise errors.InvalidShape("Given ndarray has to be 1-D or 2-D, but found", str(len(n.shape))+"-D ndarray.")
        new_data.append(new_item)

    return np.asarray(new_data)
